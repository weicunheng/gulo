# -*- coding:utf-8 _*-
import datetime
import time
from pytz import timezone, country_timezones, utc

"""
处理本地化时间的通常做法是 ， 先将所有的时间转换成UTC时间
使用合适的时区转换一下即可
"""


def fun1():
    timenow = (datetime.datetime.utcnow() + datetime.timedelta(hours=8))  # 将utc时间转化为本地时间
    timetext = timenow.strftime('%y%m%d')


def utc_to_local(utc_time_str, utc_format='%Y-%m-%dT%H:%M:%S.%fZ'):
    local_tz = timezone('Asia/Shanghai')
    local_format = "%Y-%m-%d %H:%M:%S"
    utc_dt = datetime.datetime.strptime(utc_time_str, utc_format)
    local_dt = utc_dt.replace(tzinfo=utc).astimezone(local_tz)
    time_str = local_dt.strftime(local_format)
    return datetime.datetime.fromtimestamp(int(time.mktime(time.strptime(time_str, local_format))))


if __name__ == '__main__':
    print()