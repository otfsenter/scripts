#!/bin/python
# _*_ coding: utf-8 _*_
# @Author   : otfsenter
import json
import threading
import time
import tkinter as tk

import requests
import multiprocessing

url_root = 'http://www.otfsenter.com/api/movie/'


def get_server():
    a = requests.get(url_root).text
    b = json.loads(a)
    return b


def update_server(url_item, val):
    status_code = requests.put(url_item, val).status_code
    return str(status_code)


def post_server(url_item, val):
    status_code = requests.post(url_item, val).status_code
    return str(status_code)


def parse_server(now_name):
    # get order for server data
    server_list = get_server()
    names = []
    for item in server_list:
        name = item.get('name', None)
        index = item.get('id', None)
        schedule = item.get('schedule', None)
        names.append(name)
        if now_name == name:
            return str(index), name, schedule

    if now_name not in names:
        return None, None, None


class Windows(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes("-topmost", True)
        self.geometry('200x90')

        self.val_name = tk.StringVar()
        self.val_schedule = tk.StringVar()

        self.label_name = tk.Label(self, text='Name: ')
        self.label_schedule = tk.Label(self, text='Schedule')
        self.entry_name = tk.Entry(self, textvariable=self.val_name)
        self.entry_schedule = tk.Entry(self, textvariable=self.val_schedule)
        # self.button = tk.Button(self, text='Start!',
        #                         command=self.judge)

        self.label_name.grid(row=0, column=0)
        self.label_schedule.grid(row=1, column=0)
        self.entry_name.grid(row=0, column=1)
        self.entry_schedule.grid(row=1, column=1)
        # self.button.grid(row=2, column=0)

        self.after_idle(self.judge)

        self.mainloop()

    def judge(self):
        self.t = threading.Thread(target=self.schedule)
        self.t.start()

    def get_episode(self):
        a = self.val_name.get()
        b = self.val_schedule.get()
        c = {"name": a, "schedule": b}
        return c

    def schedule(self):
        while 1:
            time.sleep(3)

            now_dict = self.get_episode()
            now_name = now_dict.get('name', None)
            now_schedule = now_dict.get('schedule', None)

            server_index, server_name, server_schedule = parse_server(now_name)

            if not now_name and not now_schedule:
                server_index, server_name, server_schedule = parse_server('shameless')
                self.val_name.set(server_name)
                self.val_schedule.set(server_schedule)

            if now_schedule and now_name:
                if server_index:
                    url_item = url_root + server_index + '/'
                    if now_schedule != server_schedule:
                        code_update = update_server(url_item, now_dict)
                        if not code_update.startswith('2'):
                            break
                elif 's' in now_schedule and 'e' in now_schedule:
                    code_post = post_server(url_root, now_dict)
                    if not code_post.startswith('2'):
                        break


if __name__ == '__main__':
    t = Windows()
