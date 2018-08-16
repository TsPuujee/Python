#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 10:34:10 2018

@author: geeks

Tomohiko Sakamoto’s Algorithm
"""

def dow(y, m, d):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4] #тогтмол
    y -= m<3 # сар нь 3аас бага байвал 1-ийг хасна.
    return (y + y//4 - y//100 + y//400 + t[m-1] + d) % 7 # python // хуваах үйлдэл нь бүхлээр хуваах c хэлний / үйлдэлтэй адил

day = 18
month = 8
year = 2018
week_days = ["Ням", "Даваа", "Мягмар", "Лхагва", "Пүрэв", "Баасан", "Бямба"]
print(week_days[dow(year, month, day)]);
