# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:52:17 2018

@author: Geek

Ханойн цамхаг рекурсив

"""

def Шилжүүл(авах, байрлуул):
    print(str(авах) + " аас " + str(байрлуул) +"руу шилжүүл")

def Цамхаг(тоо, эхлэ, дамж, байрлуул):
    if тоо == 1:
        Шилжүүл(эхлэ, байрлуул)
    else:
        Цамхаг(тоо-1, эхлэ, байрлуул, дамж)
        Цамхаг(1, эхлэ, дамж, байрлуул)
        Цамхаг(тоо-1, дамж, эхлэ, байрлуул)
        
цамхагынтоо=int(input())
print("Дискийг шилжүүлсэн тоо ",цамхагынтоо**2-1)
Цамхаг(цамхагынтоо,"1-р цамхаг","2-р цамхаг","3-р цамхаг")

Шилжүүлэхтоо=(2**цамхагынтоо)-1
print("Дискийг шилжүүлсэн тоо "+str(Шилжүүлэхтоо))