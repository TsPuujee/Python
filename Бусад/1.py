# import random as haha
import math
a = 121
b = True
for i in range(2, int(math.sqrt(a))+1, 1):
    print(i)
    if a%i==0:
        b = False
        break
if(b==True):
    print("anhnii too mon")
else:
    print("anhnii too bish")

