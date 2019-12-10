#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
一维数组
"""
user_input = input("请输入数组,以逗号分隔：\n").strip()
user_list = [int (n) for n in user_input.split(',')]
print(user_list)

