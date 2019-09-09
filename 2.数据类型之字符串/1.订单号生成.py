# -*- coding:utf-8 _*-
import datetime
import time


def __next_id():
    _inum = [10000]

    def _next():
        if _inum[0] >= 99999:
            _inum[0] = 10000
        _inum[0] += 1
        _prefix = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        print(int("%s%s" % (_prefix, _inum[0])))

    return _next


nextid = __next_id()


def __next_id1():
    _inum = [10000]

    def _next():
        if _inum[0] >= 99999:
            _inum[0] = 10000
        _inum[0] += 1
        _prefix = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        print(int("%s%s" % (_prefix, _inum[0])))

    return _next


nextid1 = __next_id1()

if __name__ == '__main__':
    nextid()
