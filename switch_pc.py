#!/usr/bin/env python
# coding: utf-8

import os
import sys

flag = sys.argv[1]

if flag == '0':
    os.system('systemctl set-default multi-user.target')
elif flag == '1':
    os.system('systemctl set-default graphical.target')
else:
    print('error')
