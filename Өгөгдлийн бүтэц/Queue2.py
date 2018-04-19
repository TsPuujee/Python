# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 21:02:15 2018

@author: Geek

Дараалал холбоост
"""
import random as R

class Зангилаа(object):
    def __init__(self, утга):
        self.утга = утга
        self.дараагийн = None
class Дараалал(object):
    def __init__(self):
        self.урдТал = None
        self.ардТал = None
    def гаргах(self):
        if self.урдТал:
            утга = self.урдТал.утга
            self.урдТал = self.урдТал.дараагийн
            return утга
        raise Exception('Дараалал хоосон.')
    def оруулах(self, утга):
        шинэ = Зангилаа(утга)
        if self.урдТал:
            self.ардТал.дараагийн = шинэ
        else:
            self.урдТал = шинэ
        self.ардТал = шинэ
    def __len__(self):
        гүй = self.урдТал
        if гүй:
            тоо = 1
            гүй = гүй.дараагийн
            while гүй:
                тоо += 1  
                гүй = гүй.дараагийн
        return тоо
    def __str__(self):
        түр = self.урдТал
        if түр:
            буц=str(түр.утга)
            түр = түр.дараагийн
            while түр:
                буц=str(буц)+" "+str(түр.утга) 
                түр = түр.дараагийн
        return буц
    
    def дээд(self):
        return self.урдТал.утга

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
   
