# -*- coding:utf-8 _*-
from operator import itemgetter
from itertools import groupby

if __name__ == '__main__':
    l = [
        {"date": "2018-12-12", "msg": "订单1001创建"},
        {"date": "2018-12-15", "msg": "订单1005创建"},
        {"date": "2018-12-13", "msg": "订单1004创建"},
        {"date": "2018-12-12", "msg": "订单1002创建"},
        {"date": "2018-12-16", "msg": "订单1006创建"},
        {"date": "2018-12-12", "msg": "订单1003创建"},
    ]

    l.sort(key=itemgetter("date"))
    for date, item in groupby(l, key=itemgetter("date")):
        print(date)
        for i in item:
            print(i)
