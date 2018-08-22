#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 链式函数调用


def product(a, b):
    return a * b


def add(a, b):
    return a + b


b = True
print(product if b else add(5, 7))

