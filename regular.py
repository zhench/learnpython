# -*- coding:utf -*-

import re


s=r'ABC\-001'
m=re.match(s,'ABC-001')
print(m)

m=re.match(r'^\d{3}\-\d{3,8}$','010-12345')
print(m)
s=re.split(r'[\s\,\;]+','a,b  c,,d;f')
print(s)

m=re.match(r'^(\d{3})\-(\d{3,8})$',"010-123578")
print(m.groups())

sts_re_email=r'^\w+\@\w+\.[com|cn]'
m=re.match(sts_re_email,'someone@gmail.com')
print(m)
m=re.match(sts_re_email,'some.one#gmail.com')
print(m)
m=re.match(sts_re_email,'0someone@gmail.com')
print(m)