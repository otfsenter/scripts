#!/usr/bin/python

import json
import pprint
import subprocess
import time
import functools
import tkinter

import requests

account = ''
password = ''
call = ''

url_login = "url_login"
url_data = "url_json"
titles_list = []

login_dict = {
    "data": "multi_values"
        }

class Reminder(object):
    def __init__(self, word_text):
        self.root = tkinter.Tk()
        self.root.overrideredirect(True)
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(),
                                                self.root.winfo_screenheight()))
        self.root.configure(bg='black')
        tkinter.Label(self.root, text=word_text, fg='white', bg='black',
                      font=('Helvetica', 30)).place(anchor='center',
                                                    relx=0.5,
                                                    rely=0.5)
        self.root.after_idle(self.show)

    def hide(self):
        self.root.withdraw()
        self.root.quit()

    def show(self):
        self.root.deiconify()
        self.root.after(1000 * 2, self.hide)

    def start(self):
        self.root.mainloop()


def prompt():
    msg = 'You have a shield need to process!'
    titles_rm_ser_list = []
    for i in titles_list:
        if not str(i).startswith('Service'):
            titles_rm_ser_list.append(str(i))

    if len(titles_rm_ser_list) < 2:
        root = Reminder(msg)
        root.start()
    elif titles_rm_ser_list[-2] != titles_rm_ser_list[-1]:
        root = Reminder(msg)
        root.start()


count = 1
while 1:
    with requests.session() as s:
        s.post(url_login, data=login_dict)
        resp = s.get(url_data).text

    response = json.loads(resp)
    tasks = response['result']

    type_list = []
    for each in tasks:
        type_of_flow = each.get('processDefinitionName', None)
        process_form = each.get('processForm', None)
        start_time_string = process_form.get('startTimeString', None)
        title = process_form.get('title', None)

        print(f"index {count}: {title} {start_time_string}")

        type_list.append(type_of_flow)
        titles_list.append(title)

    if 'monitor' in type_list:
        prompt()

    titles_list = [] if len(titles_list) > 1000 else titles_list
    count += 1

    time.sleep(30)
