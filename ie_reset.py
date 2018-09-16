#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2017/10/20 9:36
# @Author   : otfsenter
# @File     : modify_proxy.py
import ctypes
import subprocess
import time
import win32gui as gui

import win32con


def get_child_windows(parent):
    if not parent:
        return

    hwnd_child_list = []
    gui.EnumChildWindows(parent, lambda child, param: param.append(child), hwnd_child_list)
    return hwnd_child_list


def click_handle(name, index=0):
    hwnd = gui.FindWindow(0, name)
    handle_list = get_child_windows(hwnd)
    button = handle_list[index]
    ctypes.windll.user32.SwitchToThisWindow(hwnd, True)
    gui.SendMessage(button, win32con.BM_CLICK, 0, 0)


def click():
    time.sleep(1)
    name_ie = u'Internet Category'

    click_handle(name_ie, 15)


def open_ie_settings():
    subprocess.Popen('rundll32.exe shell32.dll,Control_RunDLL inetcpl.cpl,,4')
    click()

if __name__ == '__main__':
    open_ie_settings()
