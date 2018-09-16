#!/bin/python
# _*_ coding: utf-8 _*_
# @Author   : otfsenter

import tkinter as tk
import threading
import time

import psutil

key = list(psutil.net_io_counters(pernic=True).keys())[0]


def seconds():
    in_flow = psutil.net_io_counters(pernic=True).get(key).bytes_recv
    out_flow = psutil.net_io_counters(pernic=True).get(key).bytes_sent

    return int(in_flow), int(out_flow)


class Windows(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes("-topmost", True)
        # self.event = event
        self.geometry('200x90')

        self.val_in = tk.StringVar()
        self.val_out = tk.StringVar()

        self.label_in = tk.Label(self, text='Incoming')
        self.label_out = tk.Label(self, text='Outgoing')
        self.entry_in = tk.Entry(self, textvariable=self.val_in)
        self.entry_out = tk.Entry(self, textvariable=self.val_out)
        self.button = tk.Button(self, text='Start!',
                                command=self.judge)

        self.label_in.grid(row=0, column=0)
        self.label_out.grid(row=1, column=0)
        self.entry_in.grid(row=0, column=1)
        self.entry_out.grid(row=1, column=1)
        self.button.grid(row=2, column=0)

        self.mainloop()

    def judge(self):
        self.t = threading.Thread(target=self.schedule)
        self.t.start()

    def schedule(self):
        in_old, out_old = seconds()
        while 1:
            time.sleep(1)
            in_new, out_new = seconds()
            net_in = (in_new - in_old) / 1024
            net_out = (out_new - out_old) / 1024

            net_in = str('%.2f' % net_in)
            net_out = str('%.2f' % net_out)

            in_big = net_in.split('.')[0]
            in_small = net_in.split('.')[1]

            out_big = net_out.split('.')[0]
            out_small = net_out.split('.')[1]

            net_in = net_in + 'KB/s'
            net_out = net_out + 'KB/s'

            if in_big == '0':
                if in_small.startswith('0'):
                    net_in = in_small[1:] + 'Bit/s'
                else:
                    net_in = in_small+ 'Bit/s'

            if out_big == '0':
                if out_small.startswith('0'):
                    net_out = out_small[1:] + 'Bit/s'
                else:
                    net_out = out_small + 'Bit/s'

            if len(in_big) > 3:
                net_in = net_in.split('.')[0][0] + '.' + net_in.split('.')[0][1:3] + "Mb/s"
            if len(out_big) > 3:
                net_out = net_out.split('.')[0][0] + '.' + net_out.split('.')[0][1:3] + "Mb/s"

            self.val_in.set(net_in)
            self.val_out.set(net_out)

            in_old = in_new
            out_old = out_new


if __name__ == '__main__':
    t = Windows()
