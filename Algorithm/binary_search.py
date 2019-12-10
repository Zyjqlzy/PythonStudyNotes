#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
二分查找
有序数组中查找某个元素
"""


def create_list():
    user_input = input("请输入有序数组，逗号分隔：\n").strip()
    user_list = [int(n) for n in user_input.split(',')]
    print(user_list)
    return user_list


def binary_sort(sorted_list, n):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_item = sorted_list[mid]
        if mid_item == n:
            return mid
        if mid_item > n:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":
    user_list = create_list()
    item = int(input("请输入想匹配的元素：\n"))
    result = binary_sort(user_list, item)
    if result is not None:
        print("{} found at positions: {}".format(item, result))
    else:
        print("found None")
