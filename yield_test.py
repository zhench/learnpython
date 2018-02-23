# -*- coding:utf-8 -*-

def gen_one():
    i=0
    i+=1
    yield i
    i+=2
    yield i
t=gen_one()
print(next(t))
print(next(t))
print(next(t))