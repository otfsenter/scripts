#!/usr/bin/python3
# coding: utf-8

import os
import subprocess

file_profile = '/etc/profile'

items = []
with open(file_profile) as f:
    for i in f:
        i = i.strip()
        if 'proxy' in i.lower():
            if '#' not in i:
                i = '# ' + i
                items.append(i)
                os.system('systemctl stop shadowsocks')
                os.system('systemctl stop privoxy')

                os.system('unset http_proxy')
                os.system('unset https_proxy')
                os.system('unset ftp_proxy')
                os.system('unset all_proxy')
                os.system('unset no_proxy')

            else:
                i = i.replace('# ', '')
                items.append(i)
                os.system('systemctl start shadowsocks')
                os.system('systemctl start privoxy')
        else:
            items.append(i)


with open(file_profile, 'w') as f:
    f.write('\n'.join(items) + '\n')


os.system('source /etc/profile')
os.system('systemctl status shadowsocks')
os.system('systemctl status privoxy')
