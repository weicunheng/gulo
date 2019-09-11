# -*- coding:utf-8 _*-
import datetime
d = datetime.datetime(2019,4,23,15,33,29).now()
m = d + datetime.timedelta(days=1)
print((round(m.timestamp() / 1000)))