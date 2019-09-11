# -*- coding:utf-8 _*-
import calendar
from datetime import datetime, date, timedelta


def get_date_range(start_date=None):
    if not start_date:
        start_date = date.today().replace(day=1)
    week, days = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days)
    return start_date, end_date


if __name__ == '__main__':
    start_date, end_date = get_date_range()
    while start_date < end_date:
        print(start_date)
        start_date += timedelta(days=1)
