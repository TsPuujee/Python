# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 12:24:55 2018

@author: Geek

Class 
"""

#################
## EXAMPLE: simple Цэг class
#################
class Цэг(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def зай(self, өөр):
        x_diff_sq = (self.x-өөр.x)**2
        y_diff_sq = (self.y-өөр.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

а = Цэг(3,4)
б = Цэг(0,0)
а.x=4
print(а)
print(б)
print(а.зай(б), " ")