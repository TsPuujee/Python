# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 22:27:42 2018

@author: Geek

1996 оны 01 сарын 20ноос 2018 оны 01 сарын 21 хүртэл 
хэдэн жил 01 сарын 20нд бямба гариг байсныг тоолох
"""
import datetime as сан
ГаригаагынТөрсөнОн=1996
Одоо=2018
давхцсанӨдөр=0
for он in range(ГаригаагынТөрсөнОн, Одоо+1):
    if(сан.date(он,8,15).weekday()==3):
        давхцсанӨдөр=давхцсанӨдөр+1
print("Бямбагариг-н төрсөн өдөр ",давхцсанӨдөр," удаа бямба гаригт тохиосон.\n")
for он in range(ГаригаагынТөрсөнОн, Одоо+1):
    if(сан.date(он,8,15).weekday()==3):
        print(он," онд Бямбагариг-н төрсөн өдөр Бямба гаригт байсан.")
