# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 20:43:18 2018

@author: Geek

дараалал 2 стек ашигласан
"""

class Дараалал(object):
    def __init__(self):
        self.ор_стек = []
        self.гар_стек = []
    def оруулах(self, item):
        return self.ор_стек.append(item)
    def гаргах(self):
        if self.гар_стек:
            return self.гар_стек.pop()
        while self.ор_стек:
            self.гар_стек.append(self.ор_стек.pop())
        if not self.гар_стек:
            raise Exception("Queue empty!")
        return self.гар_стек.pop()
    def __len__(self):
        return len(self.ор_стек) + len(self.гар_стек)
    def __str__(self):
        return str(self.ор_стек+self.гар_стек)
    def дээд(self):
        if self.гар_стек:
            return self.гар_стек[-1]
        while self.ор_стек:
            self.гар_стек.append(self.ор_стек.pop())
        if self.гар_стек:
            return self.гар_стек[-1]
        else:
            return None
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
    