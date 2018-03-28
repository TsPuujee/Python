# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 10:25:42 2018

@author: Geek
"""

import random as R
дар=[]
def дүүргэ():
    дар.clear()
    for i in range(11):
        түр=R.randint(1,210)
        дар.append(түр)

def SelectionSortS(дар):
    for i in range(0,len(дар)):
        mini = i
        for j in range(i,len(дар)): 
            if (дар[j] < дар[mini]):
                mini = j 
        дар[mini], дар[i] = дар[i], дар[mini]
    return дар

дүүргэ()
print(дар)
print(SelectionSortS(дар))
