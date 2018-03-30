#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 14:38:14 2018

@author: geeks

Radix Sort
"""

import random as санамсаргүй
дар=[]
def дүүргэ():
    дар.clear()
    for i in range(15):
        түр=санамсаргүй.randint(1,210)
        дар.append(түр)


def СууриарЭрэмбэлэх(дар):
  Суурь = 10
  ХамгийнУрт = False
  түр , байрлал = -1, 1

  while not ХамгийнУрт:
    ХамгийнУрт = True
    хэсэг = [list() for _ in range(Суурь)]
    for  i in дар:
      түр = i // байрлал
      хэсэг[түр % Суурь].append( i )
      if ХамгийнУрт and түр > 0:
        ХамгийнУрт = False
    a = 0
    for b in range( Суурь ):
      түр1 = хэсэг[b]
      for i in түр1:
        дар[a] = i
        a += 1
    байрлал *= Суурь
  return дар
    
дүүргэ()
print(дар)
print(СууриарЭрэмбэлэх(дар))
