# -*- coding:utf-8 _*-
"""
通过某几个字段来排序字典
"""
from operator import itemgetter

if __name__ == '__main__':
    rows = [
        {'id': 1002, "age": 1},
        {'id': 1001, "age": 9},
        {'id': 1004, "age": 3},
        {'id': 1003, "age": 6},
        {'id': 1000, "age": 9},
    ]

    print(sorted(rows, key=itemgetter('id')))
    print(sorted(rows, key=itemgetter('age')))
    print(sorted(rows, key=itemgetter('age', 'id')))
