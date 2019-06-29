def calc(Pers):
    hogshin = Pers[0]
    ondorhun = Pers[0]
    for a in Pers:
        if(hogshin[2]<a[2]):
               hogshin = a
        if(ondorhun[0] < a[0]):
               ondorhun = a
    return (hogshin, ondorhun)

persons = ((162,"Чингис хаан", 45),(186, "Өгэдэй", 14),(126,"Гүег хаан", 5), (129,"Мөнх хаан", 98))
(hogshin1, ondorhun1) = calc(persons)
print("Хамгийн хөгшин настай хүний нэр :", hogshin1[1])
print("Хамгийн бага өндөр хүний нас :", ondorhun1[2])
