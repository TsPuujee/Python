# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:26:40 2018

@author: Geek

Newton-Raphson-ны язгуур гаргах арга
"""
алдаа = 0.000000000001
тоо = 64
хариу = тоо/2

while(abs(хариу*хариу - тоо) >= алдаа):
    хариу = хариу - (((хариу**2) - тоо)/(2*хариу))
    print(хариу)
print(str(тоо)+" гэсэн тооны язгуур бол "+ str(хариу))

