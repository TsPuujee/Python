# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 15:08:46 2018

@author: geeks

"bogus-Буруу хуурамч гэсэн үг"-ээс гаралтай.
"""
import random as санамсаргүй
дар=[]
def дүүргэ():
    дар.clear()
    for i in range(5):
        түр=санамсаргүй.randint(1,210)
        дар.append(түр)

def bogosort(дар):
    def ЭрэмбэлэгдсэнЭсэх(дар):
        if len(дар) < 2:
            return True
        for i in range(len(дар) - 1):
            if дар[i] > дар[i + 1]:
                return False
        return True

    while not ЭрэмбэлэгдсэнЭсэх(дар):
        санамсаргүй.shuffle(дар)
    return дар

дүүргэ()
print(дар)
print(bogosort(дар))