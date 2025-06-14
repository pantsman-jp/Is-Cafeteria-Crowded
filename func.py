# from jpholiday import is_holiday
from datetime import datetime, date, timezone, timedelta
from sqlite3 import connect


def get_jst():
    return datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=9)))


def get_hhmm():
    """
    get current time(JST)
    return [hour, min]
    by pantsman
    """
    hhmm = str(get_jst())
    return [int(hhmm[11:13]), int(hhmm[14:16])]


def split_ymd(ymd=str(get_jst())[:10]):
    """引数の日付形式は `yyyy-mm-dd`::str にすること。"""
    return [int(x) for x in ymd.split("-")]


# def get_type(ymd=split_ymd()):
#     today = date(ymd[0], ymd[1], ymd[2])
#     if is_holiday(today):
#         return 6
#     return today.weekday()


def timestamp():
    """yyyy-mm-dd hh:mm:ss"""
    return str(get_jst())[:19]


def insert(ipaddr, state):
    conn = connect("cafeteria_status.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO vote (timestamp, ip, status) VALUES (?, ?, ?)",
        (timestamp(), ipaddr, int(state)),
    )
    conn.commit()
    cur.close()
    conn.close()


def print_table():
    conn = connect("cafeteria_status.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM vote")
    print(cur.fetchall())
    cur.close()
    conn.close()


def classify(n):
    if n == 0:
        return "情報なし"
    if n <= 1.5:
        return "空いている"
    if n >= 2.5:
        return "混んでいる"
    return "普通"


def calc_time(now, min):
    return (now - timedelta(minutes=min)).strftime("%Y-%m-%d %H:%M:%S")


def get_avg(m1, m2):
    """
    take average from m1 min before to m2 min before.
    m1 must be greater than m2
    """
    conn = connect("cafeteria_status.db")
    cur = conn.cursor()
    now = get_jst()
    cur.execute(
        "SELECT AVG(status) FROM vote WHERE timestamp >= ? AND timestamp <= ?",
        (calc_time(now, m1), calc_time(now, m2)),
    )
    ret = cur.fetchone()[0]
    cur.close()
    conn.close()
    if ret is None:
        return 0
    return ret


def is_enough_data(xs, threshold):
    return len([x for x in xs if x == 0]) > threshold


def get_trend(min):
    data = [get_avg(m, m - 1) for m in range(min, 0, -1)]
    if is_enough_data(data, 6):
        return "情報不足"
    diff = [x - y for (x, y) in zip(data, data[1:])]
    trend = sum(diff) / len(diff)
    if trend > 0.3:
        return "これから混み始めるでしょう"
    if trend < -0.3:
        return "これから空き始めるでしょう"
    return "混雑状況に変化はないでしょう"
