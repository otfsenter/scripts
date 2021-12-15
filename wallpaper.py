"""
play video as wallpaper in desktop
require: pywin32
"""

import subprocess
import time
import win32gui
import win32con

r = r"D:\ffmpeg\bin\ffplay.exe D:\thunder\wallpaper\t.mp4 -noborder -x 1920 -y 1080 -loop 0"
subprocess.Popen(r)
time.sleep(.5)

progman = win32gui.FindWindow('Progman', None)
cryptic_params = (0x52c, 0, 0, 0, 100)
win32gui.SendMessageTimeout(progman, *cryptic_params)
ffplay = win32gui.FindWindow('SDL_app', None)
win32gui.SetParent(ffplay, progman)
def_view = win32gui.FindWindowEx(progman, 0, 'SHELLDLL_DefView', None)
if def_view:
    worker_w = win32gui.FindWindowEx(0, progman, 'WorkerW', None)
    win32gui.ShowWindow(worker_w, win32con.SW_HIDE)


