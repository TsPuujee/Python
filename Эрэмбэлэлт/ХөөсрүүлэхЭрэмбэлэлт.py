# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 16:57:11 2018

@author: Geek
"""
import random as санамсаргүй
дар=[]
def дүүргэ():
    дар.clear()
    for i in range(5):
        түр=санамсаргүй.randint(1,210)
        дар.append(түр)

def ХөөсрүүлэхЭрэмбэлэлт(дар):
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
print(ХөөсрүүлэхЭрэмбэлэлт(дар))
