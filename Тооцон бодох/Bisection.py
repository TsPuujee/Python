# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:26:40 2018

@author: Geek

Bisection-ны язгуур гаргах арга
"""
тоо = 25.0
алдаа = 0.00000000000001
давт_тоо = 0
бага = 0.0
их = тоо
хариу = (их + бага)/2.0
while abs(хариу**2 - тоо) >= алдаа:
    print('бага = ' + str(бага) + ' их = ' + str(их) + ' хариу = ' + str(хариу))
    давт_тоо += 1
    if(хариу**2 < тоо):
        бага = хариу
    else:
        их = хариу
    хариу = (их + бага)/2.0
print('Давталтын тоо = ' + str(давт_тоо))
print(str(тоо) + ' гэсэн тооны язгуур бол ' + str(хариу))
