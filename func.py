from jpholiday import is_holiday
from datetime import datetime, date, timezone, timedelta
from sqlite3 import connect


def get_jst():
    return datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=9)))


def get_hhmm():
    """
    get current time(JST)
    by pantsman
    """
    hhmm = str(get_jst())
    return [int(hhmm[11:13]), int(hhmm[14:16])]


def split_ymd(ymd=str(get_jst())[:10]):
    """引数の日付形式は `yyyy-mm-dd`::str にすること。"""
    return [int(x) for x in ymd.split("-")]


def get_type(ymd=split_ymd()):
    today = date(ymd[0], ymd[1], ymd[2])
    if is_holiday(today):
        return 6
    return today.weekday()


def timestamp():
    """yyyy-mm-dd hh:mm:ss"""
    return str(get_jst())[:19]


def make_db():
    conn = connect("cafeteria_status.db")
    conn.close()


def make_table():
    conn = connect("cafeteria_status.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE vote (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp TEXT NOT NULL, ip TEXT NOT NULL, status INTEGER NOT NULL)"
    )
    conn.commit()
    conn.close()


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
    if n is None:
        return "情報なし"
    if n <= 1.5:
        return "空いている"
    if n >= 2.5:
        return "混んでいる"
    return "普通"


def get_avg(min):
    """recent status"""
    conn = connect("cafeteria_status.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT AVG(status) FROM vote WHERE timestamp >= ?",
        ((get_jst() - timedelta(minutes=min)).strftime("%Y-%m-%d %H:%M:%S"),),
    )
    ret = cur.fetchone()[0]
    cur.close()
    conn.close()
    return ret


def get_trend():
    now, before = get_avg(10), get_avg(20)
    if (now is None) or (before is None):
        return "情報不足です"
    diff = now - before
    if diff > 0.3:
        return "これから混み始めるでしょう"
    if diff < -0.3:
        return "これから空き始めるでしょう"
    return "混雑状況に変化はないでしょう"


# print(get_avg(10))
