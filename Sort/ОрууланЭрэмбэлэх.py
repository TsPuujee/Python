#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 14:29:06 2018

@author: geeks


Selection Sort
"""

import random as санамсаргүй
дар=[]
def дүүргэ():
    дар.clear()
    for i in range(5):
        түр=санамсаргүй.randint(1,210)
        дар.append(түр)

def СонгонЭрэмбэлэх(дар):
    for i in range(1, len(дар)):
        j = i
        while j > 0 and дар[j-1] > дар[j]:
            дар[j-1], дар[j] = дар[j], дар[j-1]
            j -= 1
    return дар
    
дүүргэ()
print(дар)
print(СонгонЭрэмбэлэх(дар))

