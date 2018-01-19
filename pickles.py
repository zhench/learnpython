# -*- coding:utf-8 -*-
import pickle
import os
d=dict(name='Bob',age=20,score=88)
print(pickle.dumps(d))
f=open('tt.txt','wb')
f.write(pickle.dumps(d))
f.close()
fb=open('tt.txt','rb')
di=pickle.load(fb)
fb.close()
print(di)