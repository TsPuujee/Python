# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 20:08:12 2018

@author: geeks
"""
def pal(Str):
    Str1=Str[::-1]
    if(Str1==Str):
        return True
    else:
        return False
s=input()
if(pal(s)):
    print(s+" Тэмдэгт мөр палиндроме.")
else:
    print(s+" Тэмдэгт мөр палиндроме биш.")
print(s[0:5])