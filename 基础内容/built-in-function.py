#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
abs(x):返回x的绝对值
"""
print(abs(-3))

"""
all(iterable):判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
如果iterable的所有元素不为0、''、False或者iterable为空，all(iterable)返回True，否则返回False；
注意：空元组、空列表返回值为True，这里要特别注意。
"""
print(all(['a', 'b', 'c', '']))  # 列表存在一个为空的元素，返回False
print(all(['a', 'b', 'c', 'd']))  # 列表都有元素，返回True
print(all([0, 1, 2, 3, 4, 5, 6]))  # 列表里存在为0的元素 返回False

print(all(('a', 'b', 'c', '')))  # 元组存在一个为空的元素，返回Fasle
print(all(('a', 'b', 'c', 'd')))  # 元组都有元素，返回True
print(all((0, 1, 2, 3, 4, 5)))  # 元组存在一个为0的元素，返回Fasle

print(all([]))  # 空列表返回 True
print(all(()))  # 空元组返回 True

"""
any():判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
如果都为空、0、false，则返回false，如果不都为空、0、false，则返回true。
"""
print(any(['a', 'b', 'c', '']))  # 列表存在一个为空的元素，返回True
print(any(['a', 'b', 'c', 'd']))  # 列表都不为空，返回True
print(any([0, '', False]))  # 列表里的元素全为  0,'',False  返回False

print(any(('a', 'b', 'c', '')))  # 元组存在一个为空的元素，返回True
print(any(('a', 'b', 'c', 'd')))  # 元组都有元素，返回True
print(any((0, '', False)))  # 元组里的元素全为  0,'',False  返回False

print(any([]))  # 空列表返回 False
print(any(()))  # 空元组返回 False
