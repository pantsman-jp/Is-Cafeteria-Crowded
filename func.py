# from jpholiday import is_holiday
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


def split_ymd(ymd=str(date.today())):
    """引数の日付形式は `yyyy-mm-dd` にすること。"""
    return [int(x) for x in ymd.split("-")]


# def get_type(ymd=split_ymd()):
#     x = date(ymd[0], ymd[1], ymd[2])
#     if is_holiday(x):
#         return "hd"
#     type = x.weekday()
#     if type <= 4:
#         return "wd"
#     if type == 5:
#         return "st"
#     return "hd"


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


def get_avg(min):
    conn = connect("cafeteria_status.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT AVG(status) FROM vote WHERE timestamp >= ?",
        ((get_jst() - timedelta(minutes=min)).strftime("%Y-%m-%d %H:%M:%S"),),
    )
    avg = cur.fetchone()[0]
    cur.close()
    conn.close()
    return avg


# print(timestamp(), split_ymd(), get_type())
# print(timestamp())
# print_table()
# print(get_avg(10))
