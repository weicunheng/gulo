# -*- coding:utf-8 _*-
from datetime import datetime, timedelta

# 几天后

now = datetime.now()
print(now + timedelta(days=3))