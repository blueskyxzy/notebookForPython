#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 转置二维数组
original = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*original)
print(list(transposed))
