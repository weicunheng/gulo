# -*- coding:utf-8 _*-
"""
有序字典
    精确控制JSON编码后字段的顺序，可以使用 OrderedDict 先构建数据，然后在序列化。
注意：
    一个 OrderedDict 的大小是一个普通字典的两倍，因为它内部维护着另外一个链表。
"""
import json
from collections import OrderedDict


if __name__ == '__main__':

    map = OrderedDict()
    map["a"] = 1
    map["b"] = 2

    print(json.dumps(map))
