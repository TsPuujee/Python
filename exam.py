# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:47:51 2018

@author: Geek

Newton-Raphson-ны язгуур гаргах
"""


алдаа = 0.000000000001
тоо = 64
хариу = тоо/2

while(abs(хариу*хариу - тоо) >= алдаа):
    хариу = хариу - (((хариу**2) - тоо)/(2*хариу))
    print(хариу)
print(str(тоо)+" гэсэн тооны язгуур бол "+ str(хариу))


print(55//2.0)

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
#
#fil=open('pi_digits.txt','a')
#print(fil.read())
#fil.writelines("hi puujee")
#fil.close()
