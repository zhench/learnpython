#!/usr/bin/env python
import os

output=os.popen('sudo poweroff')

print output.read()
