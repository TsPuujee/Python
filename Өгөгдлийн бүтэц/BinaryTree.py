# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 18:36:36 2018

@author: Geek

Хоёртын хайлтын мод
"""
import collections as col
import random as R
class ХМод(object):
    def __init__(self, утга):
        self.утга = утга
        self.зүүн = None
        self.баруун = None
        
    def НавчЭсэх(self):
        return self.зүүн is None and self.баруун is None
    
    def нэм(self, утга1):
        if (self==None):
            self=ХМод(утга1)
        if(self.утга>утга1):
            if (self.зүүн==None):
                self.зүүн=ХМод(утга1)
            else:
                self.зүүн.нэм(утга1)
        else:
            if (self.баруун==None):
                self.баруун=ХМод(утга1)
            else:
                self.баруун.нэм(утга1)
    
    def хэвлэ(self):
        if not(self==None):
            if not(self.зүүн==None):
                self.зүүн.хэвлэ()
            print(self.утга)
            if not(self.баруун==None):
                self.баруун.хэвлэ()
                
    def хэвлэ1(self):
        if not(self==None):
            if not(self.баруун==None):
                self.баруун.хэвлэ1()
            print(self.утга)
            if not(self.зүүн==None):
                self.зүүн.хэвлэ1()
                
    def хэвлэ2(self):
        if not(self==None):
            print(self.утга)
            if not(self.зүүн==None):
                self.зүүн.хэвлэ2()
            if not(self.баруун==None):
                self.баруун.хэвлэ2()
            
            
            
мод = ХМод(10)
for i in range(5):
    түр=R.randint(1,20)
    мод.нэм(түр)
    print(түр)
    
print("\n")
мод.хэвлэ()
print("\n")
мод.хэвлэ1()
print("\n")
мод.хэвлэ2()