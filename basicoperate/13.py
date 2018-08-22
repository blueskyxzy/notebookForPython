#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 转换列表为逗号分隔符格式
items = ['foo', 'bar', 'xzy']
print(','.join(items))

number = [2, 3, 5, 7, 4]
print(','.join(map(str, number)))

data = [2, 'hello', 5, 33]
print(','.join(map(str, data)))

