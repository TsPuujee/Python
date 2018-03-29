# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 21:22:43 2018

@author: Geek

N^2 хугацааны үнэлгээтэй эрэмбэлтүүд
"""
import random as R
дар=[]
def дүүргэ():
    дар.clear()
    for i in range(11):
        түр=R.randint(1,210)
        дар.append(түр)
    
def insertion_sort(дар):
    for i in range(1, len(дар)):
        j = i
        while j > 0 and дар[j-1] > дар[j]:
            дар[j-1], дар[j] = дар[j], дар[j-1]
            j -= 1
    return дар

def selection_sort(дар):
    for i in range(len(дар) -1, 0, -1):
        max_j = i
        for j in range(max_j):
            if дар[j] > дар[max_j]:
                max_j = j
            дар[i], дар[max_j] = дар[max_j], дар[i]
    return дар

def gnome_sort(дар):
    i = 0
    while i < len(дар):
        if i ==0 or дар[i-1] <= дар[i]:
            i += 1
        else:
            дар[i], дар[i-1] = дар[i-1], дар[i]
            i -= 1
    return дар

дүүргэ()
print(дар)
print(insertion_sort(дар),"\n\n")
дүүргэ()
print(дар)
print(selection_sort(дар),"\n\n")
дүүргэ()
print(дар)
print(gnome_sort(дар),"\n\n")