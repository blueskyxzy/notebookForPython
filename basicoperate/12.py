#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from operator import itemgetter

# 通过 键 排序字典元素

d = {'ad': 1, 'bs': 2, 'ca': 3, 'cs': 2, 'ss': 4, 'aa': 7, 'eb': 2}
print(sorted(d.items(), key=lambda x: x[1]))

print(sorted(d.items(), key=itemgetter(1)))
print(sorted(d, key=d.get))
