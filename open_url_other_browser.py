#!/usr/bin/python
# coding: utf-8

import webbrowser

urL = 'http://baidu.com'
firefox_path = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path), 1)
webbrowser.get('firefox').open(urL)
