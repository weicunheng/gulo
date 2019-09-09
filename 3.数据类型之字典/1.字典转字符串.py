# -*- coding:utf-8 _*-
"""
对字典排序，并转成字符串
    对json进行加密时，为了和java一致
    因为python会把""(双引号)格式化成''(单引号)
"""


def dict_sorted_to_str(map):
    sorted_keys = sorted(map.keys())
    s = """{"""

    for key in sorted_keys:
        if isinstance(map[key], str):
            s += "\"" + key + "\":" + "\"" + map[key] + "\","
        elif isinstance(map[key], list):
            tmp_s = "\"" + key + "\":["

            for item in map[key]:
                tmp_s += dict_sorted_to_str(item) + ","

            tmp_s += "]"
            c, d = tmp_s.rsplit(",", 1)
            s += c + d + ","
        elif str(map[key]) == "True":
            s += "\"" + key + "\":" + "true" + ","
        elif str(map[key]) == "False":
            s += "\"" + key + "\":" + "false" + ","
        else:
            s += "\"" + key + "\":" + str(map[key]) + ","

    s += """}"""
    a, b = s.rsplit(",", 1)
    return a + b


if __name__ == '__main__':
    map = {"a": 1, "b": 2}
    print(dict_sorted_to_str(map))
