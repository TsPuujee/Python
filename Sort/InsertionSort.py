# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 10:11:00 2018

@author: Geek
"""

import random as R
дар=[]
def дүүргэ():
    дар.clear()
    for i in range(11):
        түр=R.randint(1,210)
        дар.append(түр)

def InsertionSortS(дар):
    for i in range(1, len(дар)):
        j = i
        while j > 0 and дар[j-1] > дар[j]:
            дар[j-1], дар[j] = дар[j], дар[j-1]
            j -= 1
    return дар
дүүргэ()
print(дар)
print(InsertionSortS(дар))

