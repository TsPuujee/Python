#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 14:23:28 2018

@author: geeks

"""

import random as санамсаргүй
дар=[]
def дүүргэ():
    дар.clear()
    for i in range(5):
        түр=санамсаргүй.randint(1,210)
        дар.append(түр)

def ОрууланЭрэмбэлэх(дар):
    урт = len(дар)
    for i in range(урт):
        бага = i
        for k in range(i + 1, урт):
            if дар[k] < дар[бага]:
                бага = k
        дар[бага], дар[i] = дар[i], дар[бага]
    return дар
дүүргэ()
print(дар)
print(ОрууланЭрэмбэлэх(дар))

