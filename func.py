# from jpholiday import is_holiday
from datetime import datetime, date
from sqlite3 import connect


def get_hhmm():
    hhmm = str(datetime.now())
    return [int(hhmm[11:13]), int(hhmm[14:16])]


def get_hour():
    return get_hhmm()[0]


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
    """`yyyy-mm-dd hh:mm:ss"""
    return str(datetime.now())[:19]


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


# print(timestamp(), split_ymd(), get_type())
# print(timestamp())
# print_table()
