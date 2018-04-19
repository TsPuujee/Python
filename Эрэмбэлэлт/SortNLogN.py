# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 21:52:57 2018

@author: Geek

NLogN хугацааны үнэлгээтэй эрэмбэлтүүд
"""
import random as R
import heapq

дар=[]
def дүүргэ():
    дар.clear()
    for i in range(11):
        түр=R.randint(1,210)
        дар.append(түр)
    
def quick_sort(seq):
    if len(seq) < 2 : return seq
    mid = len(seq)//2
    pi = seq[mid]
    seq = seq[:mid] + seq[mid+1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return quick_sort(lo) + [pi] + quick_sort(hi)
def heap_sort1(seq):
    h = []
    for value in seq:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

дүүргэ()
print(дар)
print(quick_sort(дар),"\n\n")
дүүргэ()
print(дар)
print(heap_sort1(дар),"\n\n")
