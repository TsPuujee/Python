# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 17:29:54 2018

@author: Geek

MergeSort
"""
import random as R
def нэгтгэ(зүүн, баруун):
    үрдүн = []
    i,j = 0,0
    while i < len(зүүн) and j < len(баруун):
        if зүүн[i] < баруун[j]:
            үрдүн.append(зүүн[i])
            i += 1
        else:
            үрдүн.append(баруун[j])
            j += 1
    while (i < len(зүүн)):
        үрдүн.append(зүүн[i])
        i += 1
    while (j < len(баруун)):
        үрдүн.append(баруун[j])
        j += 1
    print('Нэгтгэ: ' + str(зүүн) + '&' + str(баруун) + ' = ' +str(үрдүн))
    return үрдүн

def нэгтгэнЭрэмбэлэх(L):
    print('Хуваа: ' + str(L))
    if len(L) < 2:
        return L[:]
    else:
        дунд = len(L)//2
        зүүн= нэгтгэнЭрэмбэлэх(L[:дунд])
        баруун = нэгтгэнЭрэмбэлэх(L[дунд:])
        return нэгтгэ(зүүн, баруун)
        
ЖишээДараалал = [1,3]
for i in range(11):
    түр=R.randint(1,40)
    ЖишээДараалал.append(түр)

print(нэгтгэнЭрэмбэлэх(ЖишээДараалал))
