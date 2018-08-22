#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 合并字典

d1 = {'a': 3}
d2 = {'b': 5}

print(**d1, **d2)
print(d1.items())

print(dict(d1.items() | d2.items()))

d1.update(d2)
print(d1)