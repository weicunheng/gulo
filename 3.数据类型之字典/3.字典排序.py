# -*- coding:utf-8 _*-

def sorted_dict(map):
    sorted_keys = sorted(map.keys())
    secret_str = ''
    for key in sorted_keys:
        if key == 'sign':
            continue
        secret_str = secret_str + key + '=' + str(map[key]) + '&'
    return secret_str[:-1]


if __name__ == '__main__':
    map = {"a": 1, "b": 2, "d": 3, "c": 4}
    print(sorted_dict(map))
