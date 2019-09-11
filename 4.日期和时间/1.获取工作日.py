# -*- coding:utf-8 _*-
import datetime


def get_business_day(time_string, n):
    """
    在给定的日期添加n个工作日,忽略假日和周末
    :param time_string:
    :param n:
    :return:
    """
    try:
        datetime.datetime.strptime(time_string, "%Y-%m-%d")
    except:
        raise Exception("时间格式有误, 请参照%YYYY-%MM-%DD")
    current_date = datetime.datetime.strptime(time_string, "%Y-%m-%d")

    business_days_to_add = n
    while business_days_to_add > 0:
        current_date += datetime.timedelta(days=1)
        weekday = current_date.weekday()
        if weekday >= 5:  # sunday = 6
            continue
        business_days_to_add -= 1
    return current_date.strftime("%Y-%m-%d")


print(get_business_day("2019-04-30", 3))