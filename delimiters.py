#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2017/3/9 19:52
# @Author   : otfsenter
# @File     : a.py

#coding:utf-8

result = '''
sdf-asd
sdf-asd01
sdf-asd02
sdf-asd,sdf-asd01 ,sdf-asd02
aui+otfsenter+which
'''

# result = ''
# with open('tmp.txt', 'r') as f:
#     for i in f:
#         result += i
#
# print result

def split_by_separator(string='', separators=','):
    rst = [string]
    for sep in separators:
        tmp = []
        for r in rst:
            tmp.extend(map(lambda x: x.strip(), r.split(sep)))
        rst = tmp
    list_tmp = []
    [list_tmp.append(data) for data in rst if data != '']
    return reduce(lambda x, y: y in x and x or x + [y], [[], ] + list_tmp)

print split_by_separator(result, '\n,+')
