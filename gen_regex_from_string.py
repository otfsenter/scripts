#!/usr/bin/python
# coding: utf-8
import re

c = re.compile('(.)(.)\1(.)')

def get_patterns(word):
    patterns = []
    seen = []
    for letter in word:
        if letter in seen:
            patterns.append("\%d" % (seen.index(letter) + 1))
        else:
            patterns.append("(.)")
            seen.append(letter)
    return ''.join(patterns)


a = get_patterns('abac')
print(a)
