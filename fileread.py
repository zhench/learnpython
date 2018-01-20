# -*- coding:utf-8 -*-

f = open('./readme.md', 'r')
print(f)
with open('./GPL.txt', 'r') as t:
    print(t.read())

for line in f.readlines():
    print(line.strip())

filereadme=open('tt','w')
filereadme.write('Hello,world!')
filereadme.close()
with open('./readme.md','a') as filereadme:
    pass
