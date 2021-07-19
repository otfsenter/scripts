# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.messagebox import showwarning, showinfo
import time
from ctypes import *
import threading
import re

file_todo = r'D:\tmp\docs\0-todo.md'


def read_todo():
    todo_list = []
    with open(file_todo, encoding='utf-8') as f:
        for i in f:
            i = i.strip().lower()
            if re.match('^# ', i):
                todo_list.append(i)
    return '\n'.join(todo_list)


# tkinter GUI工具居中展示
def center_window(master, width, height):
    screenwidth = master.winfo_screenwidth()
    screenheight = master.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2,
                            (screenheight - height) / 2)
    master.geometry(size)


# 锁定屏幕
def close_windows():
    user32 = windll.LoadLibrary('user32.dll')
    user32.LockWorkStation()


class CareForCoders:
    def __init__(self):
        self.countdown_lb = None

    def user_setting(self):
        note = LabelFrame(root, text="说明", padx=10, pady=10,
                          fg="red", font=("黑体", '11'))
        note.grid(padx=10, pady=2, sticky=NSEW)
        index = Label(note, text='运维工程师们,久坐伤身请务必定时休息！')
        index.grid()
        lb = LabelFrame(root, text="定时设置(支持小数)", padx=10,
                        pady=10, fg="red", font=("黑体", '11'))
        lb.grid(padx=10, pady=2, sticky=NSEW)
        self.time_entry = Entry(lb)
        self.time_entry.grid(row=1, column=0)
        unit = Label(lb, text="(单位：分)")
        unit.grid(row=1, column=1, padx=5)

        self.countdown_lb = Label(text="休息倒计时:", justify=LEFT,
                                  font=("黑体", '11'))
        self.countdown_lb.grid(row=2)
        self.submit = Button(root, text="启动", width=8,
                             command=lambda: self.get_countdown(self.time_entry.get())
                             )
        self.submit.grid(row=3, column=0, pady=10)

    def get_countdown(self, countdown):
        while 1:
            try:
                _float_countdown = float(countdown)
                if _float_countdown <= 0:
                    showwarning("提示：", message="倒计时必须为正数！")
                else:
                    self.time_entry.config(state=DISABLED)
                    self.submit.config(state=DISABLED)
                    self.countdown_show(_float_countdown * 60)
            except ValueError:
                showwarning("提示：", message="请填写正确的倒计时！")

    def countdown_show(self, countdown_sec):
        while countdown_sec:
            countdown_sec -= 1
            time.sleep(1)
            self.countdown_lb.config(text="休息倒计时: %02d:%02d" %
                                          (countdown_sec // 60, countdown_sec % 60))
            root.update()
            # 为了避免突如其来的锁屏，倒计时10秒给出提示...
            if countdown_sec == 30:
                t = threading.Thread(target=self.notice)
                t.start()
            if countdown_sec < 1:
                # 启动锁屏操作
                # close_windows()
                time.sleep(3)
                self.countdown_lb.config(text="欢迎主人回来...")
                self.time_entry.config(state=NORMAL)
                self.submit.config(state=NORMAL)
                return

    def notice(self):
        message = Toplevel(root)
        message.wm_attributes('-topmost', 1)
        # center_window(message, 400, 200)
        # # Label(message, text='辛苦工作这么久了，准备休息下吧！'
        # #       , justify=CENTER, fg='red', font=("黑体", '15')).grid()
        # Label(message, text='即将锁屏！！！'
        #       , justify=CENTER, fg='red', font=("黑体", '15')).place(anchor='center',
        #                                                            relx=0.5,
        #                                                            rely=0.5)
        # self.cancel = Button(root, text="取消锁屏", width=8,
        #                      command=self.cancel_lock
        #                      )
        # time.sleep(5)
        # message.destroy()

        word_text = read_todo()
        # word_text = '辛苦工作这么久了，准备休息！'
        message.geometry("{0}x{1}+0+0".format(message.winfo_screenwidth(),
                                              message.winfo_screenheight()))
        message.configure(bg='black')
        Label(message, text=word_text, fg='white', bg='black',
              font=('黑体', 25)).place(anchor='center',
                                     relx=0.5,
                                     rely=0.5)
        time.sleep(20)
        message.destroy()


if __name__ == '__main__':
    root = Tk()
    center_window(root, 260, 200)
    root.resizable(width=False, height=False)
    root.title('盘灿帅逼制作')
    Main = CareForCoders()
    Main.user_setting()
    root.mainloop()
