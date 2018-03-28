# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 12:48:29 2018

@author: Geek
"""
a=int(input())
b=int(input())
sum=int(input())
temp=sum
temp1=temp
ans=0

while(sum!=0):
    #print(sum)
    i=int(sum/a) 
    j=int(sum/b)
    while(i!=0 and j!=0):
        if((sum-i*a)%b==0):
            if(ans<i+(sum-i*a)/b):
                ans=i+(sum-i*a)/b
                print(str(i)+" "+str(int((sum-i*a)/b))+" "+str(sum))
                temp1=sum
        if((sum-j*b)%a==0):
            if(ans<j+(sum-j*b)/a):
                ans=j+(sum-j*b)/a
                print(str(j)+" "+str(int((sum-j*b)/a))+" "+str(sum))
                temp1=sum
        i=i-1
        j=j-1
    sum=sum-1
   
print()
if(temp1!=temp):
    print(str(int(ans))+" "+str(temp-temp1))
else:
    print(str(int(ans)))