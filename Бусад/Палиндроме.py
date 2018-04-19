# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:44:54 2018

@author: Geek

Палиндроме үг шалгах
"""

def Шалга(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and Шалга(s[1:-1])

тоо=input()
if(Шалга(тоо)):
    print("Палиндроме мөн")
else:
    print("Палиндроме биш")
    
