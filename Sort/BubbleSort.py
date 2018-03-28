# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 09:45:51 2018

@author: Geek
"""

import random as R
дар=[]
def дүүргэ():
    дар.clear()
    for i in range(11):
        түр=R.randint(1,210)
        дар.append(түр)

def BubbleSortS(дар):
    соль=True
    while(соль):
        соль=False
        for i in range(0,len(дар)-1):
            if(дар[i]>дар[i+1]):
                дар[i], дар[i+1] = дар[i+1], дар[i] 
                соль=True
    return дар

дүүргэ()
print(дар)
print(BubbleSortS(дар))
