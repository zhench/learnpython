#!/usr/bin/python
# -*- coding:utf-8 -*-

def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

print(power(4))

def add_end(L=[]):
    L.append('END')
    return L

add_end()
add_end()
add_end()
print(add_end())

def person(name,age,*,city,job): #命名关键字参数
    print(name,age,city,job)
    
person('jack',23,city='beijing',job='engineer')

def f1(a,b,c=0,*args,**kw):
    print('a=',a,' b=',b,' c=',c,' args=',args,' kw=',kw)

f1(1,2)
args=(1,2,3,4)
kw={'d':99,'x':'#'}
f1(*args,**kw) #参数顺序为：必选参数，默认参数，可变参数，命名关键字参数和关键字参数
