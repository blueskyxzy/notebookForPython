#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from collections import Counter

# 找出列表中频率最高的值
a = [1, 2, 3, 4, 1, 0, 1, 2, 1, 5, 3]
print(max(set(a), key=a.count))


cnt = Counter(a)
print(cnt.most_common(3))
