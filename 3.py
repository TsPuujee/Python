# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 22:09:01 2018

@author: Geek

2 тооны үржвэр болон зэрэг олох рекурсив
"""
def Үржвэр(атоо, бтоо):
    if бтоо == 1:
        return атоо
    else:
        return атоо + Үржвэр(атоо, бтоо-1)
    
def Зэрэг(атоо, бтоо):
    if бтоо == 1:
        return атоо
    else:
        return атоо * Зэрэг(атоо, бтоо-1)
    
print("а болон б тооны үржвэр "+str(Үржвэр(2,5)))
print("а болон б тооны зэрэг "+str(Зэрэг(2,5)))