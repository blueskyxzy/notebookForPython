#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from copy import deepcopy

# 复制列表
a1 = [1, 2, 3, 4, 5]
b = a1
b[0] = 10
print(a1, b)

a2 = [1, 2, 3, 4, 5]
b = a2[:]
b[0] = 10
print(a2, b)

a = [1, 2, 3, 4, 5]
print(list(a))
print(a.copy())

x = [[1, 2], [2, 3]]
x = deepcopy(x)
print(x)
