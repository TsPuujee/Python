# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 20:26:24 2018

@author: Geek

дараалал массив
"""
import random as R

class Дараалал(object):
    def __init__(self):
        self.items = []
    def хоосонЭсэх(self):
        return self.items == []
    def оруулах(self, item):
        self.items.insert(0, item)
    def гаргах(self):
        return self.items.pop()
    def __len__(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)
    def дээд(self):
        if not self.хоосонЭсэх():
            return self.items[-1]
        else:
            raise Exception('Дараалал хоосон.')
    def size(self):
        return len(self.items)
    
дар = Дараалал()
for i in range(5):
    түр=R.randint(1,20)
    дар.оруулах(түр)
    print("Дараалалд нэмэх элемэнт бол ", түр)
    print(дар)
    
print("Дарааллын хэмжээ бол ", len(дар))
for i in range(5):
    print(дар)
    түр=дар.гаргах()
    print("Дарааллаас гарсан элемэнт бол ",түр)
    
