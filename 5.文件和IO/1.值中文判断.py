# -*- coding:utf-8 _*-

def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True


def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False


print(is_contains_chinese('哈哈'))
print(is_contains_chinese('\u54c8\u54c8\u54c8'))