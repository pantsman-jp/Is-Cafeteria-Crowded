from datetime import datetime, date
from jpholiday import is_holiday
from csv import writer


def get_hhmm():
    hhmm = str(datetime.now())
    return [int(hhmm[11:13]), int(hhmm[14:16])]


def get_hour():
    return get_hhmm()[0]


def split_ymd(ymd=str(date.today())):
    """引数の日付形式は `yyyy-mm-dd` にすること。"""
    return [int(x) for x in ymd.split("-")]


def get_type(ymd=split_ymd()):
    x = date(ymd[0], ymd[1], ymd[2])
    if is_holiday(x):
        return "hd"
    type = x.weekday()
    if type <= 4:
        return "wd"
    if type == 5:
        return "st"
    return "hd"


def timestamp():
    """`yyyy-mm-dd hh:mm:ss"""
    return str(datetime.now())[:19]


def write_csv(ipaddr, state, fname="test.csv"):
    with open(fname, mode="a") as f:
        writer(f).writerow([timestamp(), ipaddr, state])


# print(timestamp(), split_ymd(), get_type())
# print(timestamp())
