#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from collections import Counter

# 检查两个字符串是否由相同字母不同顺序组成的
print(Counter("123") == Counter("321"))
