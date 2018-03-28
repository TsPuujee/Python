# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 19:41:04 2018

@author: Geek

Стек холбоост
"""
import random as R

class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None
        
class Стек(object):
    def __init__(self):
        self.top = None
        self.тоо=0
    def хоосонЭсэх(self):
        return not bool(self.top)
    def ав(self):
        node = self.top
        if node:
            self.top = node.next
            return node.value
        else:
            raise Exception('Стек хоосон.')
    def нэм(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
    def __str__(self):
        stri=str("")
        node = self.top
        if not (node == None):
            stri=self.top.value
        else:
            return ""
        node = node.next
        while node:
            stri=str(node.value)+" "+str(stri)
            node = node.next
        return str(stri)
    
    def __len__(self):
        node = self.top
        if not (node == None):
            тоо= 1
        else:
            return 0
        node = node.next
        while node:
            тоо += 1
            node = node.next
        return тоо
   
    def дээд(self):
        return self.top.value

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
