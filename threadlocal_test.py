#!/usr/bin/python
# -*- coding:utf-8 -*-

import threading

local_school = threading.local()

def process_student():
	std=local_school.student
	local_school.student='ab'
	print('Hello, %s (in %s)' % (std,threading.current_thread().name))
	print(local_school.student)

def process_thread(name):
	local_school.student=name
	process_student()

t1=threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
t2=threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
print(t1)
t1.start()
t2.start()
t1.join()
t2.join() 
print(local_school)
