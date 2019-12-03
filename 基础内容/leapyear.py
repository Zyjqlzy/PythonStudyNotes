#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
判断年份是否为闰年
闰年计算方法：能被400整除，或者 能被4整除且不能被100整除
"""

year = int(input("请输入年份：\n"))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("%d是闰年" % year)
else:
    print("%d不是闰年" % year)
