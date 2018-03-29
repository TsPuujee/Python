# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 21:45:04 2018

@author: Geek
"""
import random as R
from collections import defaultdict

дар=[]
def дүүргэ():
    дар.clear()
    for i in range(11):
        түр=R.randint(1,210)
        дар.append(түр)
    
def count_sort(a):
    
    b, c = [], defaultdict(list)
    for x in a:
        c[x].append(x)
    for k in range(min(c), max(c) + 1):
        b.extend(c[k])
    return b

дүүргэ()
print(дар)
print(count_sort(дар),"\n\n")