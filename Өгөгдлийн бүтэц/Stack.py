# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 17:53:25 2018

@author: Geek

Стек массив
"""
import random as R

class Стек:
    def __init__(self):
        self. data = []
    def __len__(self):
        return len(self. data)
    def __str__(self):
        return str(self.data)
    def хоосонЭсэх(self):
        return len(self. data) == 0
    def нэм(self, e):
        self. data.append(e) 
    def дээд(self):
        if self.хоосонЭсэх( ):
            print("Стек хоосон")
        return self.data[-1]
    def ав(self):
        if self.хоосонЭсэх():
            print("Стек хоосон")
        return self. data.pop( )
    
S = Стек( ) 
for i in range(4):
    түр=R.randint(1,20)
    S.нэм(түр)
    print("Нэмсэн элемэнт ",түр)
    print(S)
print("\nСтекийн элментийн тоо: ",len(S))
if(S.хоосонЭсэх()):
    print("Стек хоосон")
else:
    print("Стек хоосон биш")
print(S,"\n")
for i in range(4):
    түр=S.ав()
    print("Хассан элемэнт ",түр)
    print(S)
if(S.хоосонЭсэх()):
    print("Стек хоосон")
else:
    print("Стек хоосон биш")
