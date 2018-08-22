#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 列表中最小和最大的索引
list = [40, 10, 20, 30]


def minidex(list):
    return min(range(len(list),), key=list.__getitem__)


def maxidex(list):
    return max(range(len(list),), key=list.__getitem__)


print(minidex(list))
print(maxidex(list))
