#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
选择排序
"""


def create_list():
    user_input = input("请输入数据，逗号分隔：\n").strip()
    user_list = [int(n) for n in user_input.split(',')]
    print(user_list)
    return user_list


def find_smallest_item(lst):
    smallest_item = lst[0]
    smallest_index = 0
    for i in range(1, len(lst)):
        if smallest_item > lst[i]:
            smallest_item = lst[i]
            smallest_index = i
    return smallest_index


def select_sort(lst):
    newlst = []
    for i in range(len(lst)):
        smallest = find_smallest_item(lst)
        newlst.append(lst.pop(smallest))
    return newlst


if __name__ == "__main__":
    array = create_list()
    new_array = select_sort(array)
    print("排序后的序列为：", new_array)
