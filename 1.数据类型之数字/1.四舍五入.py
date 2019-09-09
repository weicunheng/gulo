# -*- coding:utf-8 _*-
"""
四舍五入问题：
    1. round(value, ndigits)
    2. %.2f 在格式化的时候指定精度
"""
f1 = 1.2555

print(round(f1, 2))
print("%.2f" % f1)   # 1.26
print("%.2f0" % f1)  # 1.260
