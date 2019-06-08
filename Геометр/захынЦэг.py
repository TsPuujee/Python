#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat JUN 08 13:24:10 2019

@author: geeks

Convex Hull (Graham Scan)

https://www.geeksforgeeks.org/convex-hull-set-2-graham-scan/
"""

from random import random

def баруунЭргэсэнЭсэх(a, b, c):
    u = (c[0] - b[0], c[1] - b[1])
    v = (a[0] - b[0], a[1] - b[1])

    return (u[0] * v[1] - u[1] * v[0]) < 0

def graham_scan(цэгүүд):
    цэгүүд.sort()

    дээдЗахынЦэг = цэгүүд[0:2]
    for цэг in цэгүүд[2:]:
        while len(дээдЗахынЦэг) > 1 and not баруунЭргэсэнЭсэх(дээдЗахынЦэг[-2], дээдЗахынЦэг[-1], цэг):
            дээдЗахынЦэг.pop()
        дээдЗахынЦэг.append(цэг)

    доодЗахынЦэг = цэгүүд[-1:-3:-1]

    for цэг in цэгүүд[-3::-1]:
        while len(доодЗахынЦэг) > 1 and not баруунЭргэсэнЭсэх(доодЗахынЦэг[-2], доодЗахынЦэг[-1], цэг):
            доодЗахынЦэг.pop()
        доодЗахынЦэг.append(цэг)

    return дээдЗахынЦэг + доодЗахынЦэг[1:-1]

цэгүүд = [(int(random() * 10), int(random() * 10)) for _ in range(10)]
print('Цэгүүд:')
print(цэгүүд)
convex_hull = graham_scan(цэгүүд)
print('Захын цэгүүд')
print(convex_hull)