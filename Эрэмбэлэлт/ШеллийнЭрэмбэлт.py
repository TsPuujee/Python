#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 14:06:36 2018

@author: geeks
"""
import random as санамсаргүй
дар=[]
def дүүргэ():
    дар.clear()
    for i in range(15):
        түр=санамсаргүй.randint(1,210)
        дар.append(түр)

def ШеллийнЭрэмбэлт(дар):
    завсар = len(дар) // 2
    while завсар > 0:
         for i in range(завсар, len(дар)):
             val = дар[i]
             j = i
             while j >= завсар and дар[j - завсар] > val:
                 дар[j] = дар[j - завсар]
                 j -= завсар
             дар[j] = val
         завсар //= 2
    return дар

дүүргэ()
print(дар)
print(ШеллийнЭрэмбэлт(дар))