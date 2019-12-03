#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
根据半径计算圆的周长和面积
"""
import math

radius = float(input("请输入半径：\n"))
circumference = 2 * math.pi * radius
area = math.pi * math.pow(radius, 2)
print("周长为%.2f" % circumference)
print("面积为%.2f" % area)
