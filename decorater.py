#! /usr/bin/env python3
# -*- coding:utf-8 *-

# 动态增强函数

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    #wrapper.__name__=func.__name__
    return wrapper

@log
def now():
    print("2015-3-25")

f=now
f()
print(f.__name__)
print("相当于now2=log(now2):")

def now2():
    print('now2')

now2=log(now2)
now2()


def log_with_para(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print("%s %s()" % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log_with_para("excute")#在装饰器上传递参数
def now3():
    print('2015-3-5')

now3()

print("相当于now4=log_with_para('excute')(now4):")
def now4(args):
    print(args)

now4=log_with_para('excute')(now4)
now4('now4')