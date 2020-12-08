#!/usr/bin/env python

import time
import tkinter
from datetime import datetime


class Reminder(object):
    def __init__(self, word_text):
        self.root = tkinter.Tk()
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(),
                                                self.root.winfo_screenheight()))
        self.root.configure(bg='black')
        tkinter.Label(self.root, text=word_text, fg='white', bg='black',
                      font=('Helvetica', 100)).place(anchor='center',
                                                     relx=0.5,
                                                     rely=0.5)
        self.root.after_idle(self.show)

    def hide(self):
        self.root.withdraw()
        self.root.quit()

    def show(self):
        self.root.deiconify()
        self.root.after(1000 * 5, self.hide)

    def start(self):
        self.root.mainloop()


def prompt():
    msg = 'You need to sleep! now!!!'
    root = Reminder(msg)
    root.start()


def main():
    while 1:
        hour = datetime.now().hour
        # we need sleep at 0 hour
        if hour == 0:
            prompt()
        else:
            print('you don\'t need to sleep')
        time.sleep(10)


if __name__ == '__main__':
    main()
