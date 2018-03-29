#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 13:24:10 2018

@author: geeks


Tree Sort
"""

import random as санамсаргүй
дар=[]
def дүүргэ():
    дар.clear()
    for i in range(15):
        түр=санамсаргүй.randint(1,210)
        дар.append(түр)

class  Зангилаа():
    def __init__(self, утга):
        self.утга = утга
        self.зүүн = None 
        self.баруун = None 
    
    def оруул(self,утга):
        if self.утга:
            if утга < self.утга:
                if self.зүүн == None:
                    self.зүүн = Зангилаа(утга)
                else:
                    self.зүүн.оруул(утга)
            elif утга > self.утга:
                if self.баруун == None:
                    self.баруун = Зангилаа(утга)
                else:
                    self.баруун.оруул(утга)
        else:
            self.утга = утга

def inorder(үндэс, хариу):
    # Recursive travesal 
    if үндэс:
        inorder(үндэс.зүүн, хариу)
        хариу.append(үндэс.утга)
        inorder(үндэс.баруун,хариу)

def МодАшигланЭрэмбэлэх(дар):
    if len(дар) == 0:
        return дар
    үндэс =  Зангилаа(дар[0])
    for i in range(1,len(дар)):
        үндэс.оруул(дар[i])
    хариу = []
    inorder(үндэс,хариу)
    return хариу


дүүргэ()
print(дар)
print(МодАшигланЭрэмбэлэх(дар))