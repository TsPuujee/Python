# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 00:31:57 2018

@author: Geek
"""
def шалга(a):
    if a<2 or (a%2==0 and a!=2) :
        return False
    else:
        for i in range(3,a,2):
            if a%i==0:
                return False
    return True
#a=int(input("Анхны тоо эсэхийг шалгах тоог оруулна уу?\n a="))
for a in range(1,100,2):
    if(шалга(a)):
        print(str(a)+" анхны тоо мөн.")
    else:
        print(str(a)+" анхны тоо биш.")
print(sum(a for a in range(1,101,1)))