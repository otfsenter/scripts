#!/usr/bin/python
# coding: utf-8

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


get_patterns('abac')
