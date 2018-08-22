#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 移除列表中的重复元素

items = [2, 3, 2, 3, 1]
x = list(set(items))
print(x)

from collections import OrderedDict

items2 = ["axd", "dase", "xzy", "xzy"]
print(OrderedDict.fromkeys(items2).keys())
