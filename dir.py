# -*- coding:utf-8 -*-
import os
print(os.path.abspath('.'))
print(os.path.join('.','testdir'))
#os.mkdir('testdir')
#os.rmdir('tet')
print(os.path.split('/path/to/file.txt'))
print(os.path.splitext('/path/to/file.txt'))
print([x for x in os.listdir('.') if os.path.isdir(x)])