#!/usr/bin/python
import os
import tkinter
from tkinter import filedialog

import xlrd
from IPy import IP

current_dir = os.getcwd()


def is_ip(ip_str):
    try:
        IP(ip_str).iptype()
        return True
    except ValueError:
        return False


def get_des_ip(ip_list_des1):
    ip_list_error = []
    ip_list_des_func = []
    # with open('src.txt', 'r', encoding='utf-8') as f:
    for i in ip_list_des1:
        i = i.strip()
        if is_ip(i):
            ip_list_des_func.append(i)

        # TODO: put error ip to ip_list_error if ip has a wrong format.
        else:
            ip_list_error.append(i)

    return ip_list_des_func, ip_list_error


def get_src_ip():
    ip_list_src = []
    workbook = xlrd.open_workbook(label_value['text'])
    sheet = workbook.sheet_by_index(0)
    column_ip_list = sheet.col_values(7)
    for multi_str in column_ip_list:
        multi_str_list = multi_str.split(' ')
        for each_multi_str in multi_str_list:
            if not '':
                if is_ip(each_multi_str):
                    ip_list_src.append(each_multi_str.strip())
    return ip_list_src

def search_excel(ip_list_des1):
    ip_list_found_src_result = []
    ip_list_found_des = []

    ip_list_src = get_src_ip()

    ip_list_des, ip_list_error = get_des_ip(ip_list_des1)

    for each_ip_des in ip_list_des:
        for each_ip_src in ip_list_src:

            ip_prefix, ip_suffix = each_ip_src.split('/')

            if int(ip_suffix) > 19:

                if IP(each_ip_des) in IP(each_ip_src):
                    ip_list_found_src_result.append(each_ip_src)
                    ip_list_found_des.append(each_ip_des)

    ip_list_not_found = list(set(ip_list_des) - set(ip_list_found_des))
    ip_list_found_src_result = list(set(ip_list_found_src_result))

    ip_list_error1 = list(set(ip_list_error))

    msg_error = f"error ip: {';'.join(ip_list_error1)}\n\n"
    msg_not_found = f"not found ip: {';'.join(ip_list_not_found)}\n\n"
    msg_result = f"result:\n{';'.join(ip_list_found_src_result)}"

    result_str1 = msg_error + msg_not_found + msg_result

    return result_str1


def main1(ip_list_des):
    return search_excel(ip_list_des)


def get_excel_path():
    path_excel = filedialog.askopenfilename(initialdir=current_dir, title="Please choose a excel file",
                                            filetypes=(("xls file", "*.xls"), ("xlsx file", "*.xlsx"), ("All", "*.*")))
    label_value_val.set(path_excel)


def set_value_to_text():
    text_result.delete('1.0', tkinter.END)

    origin_ip_str = text_ip.get('1.0', tkinter.END)
    ip_list_des = origin_ip_str.strip().split('\n')

    result_str = main1(ip_list_des)

    text_result.insert(tkinter.END, result_str)


root = tkinter.Tk()
root.resizable(width=False, height=False)
root.geometry('900x500')

label_value_val = tkinter.StringVar()

label_top = tkinter.Label(root, text='                            ')
label_prompt = tkinter.Label(root, text='name for excel: ')
label_value = tkinter.Label(root, textvariable=label_value_val)
label_empty_find_excel = tkinter.Label(root, text='    ')
button = tkinter.Button(root, text='choose excel file', command=get_excel_path)

label_empty1 = tkinter.Label(root, text='                                     ')
label_ip_prompt = tkinter.Label(root, text='Please input ip list below')
text_ip = tkinter.Text(root, height='10')
label_empty2 = tkinter.Label(root, text='                                     ')

text_result = tkinter.Text(root, height='15')
label_empty_search = tkinter.Label(root, text='    ')
button_search = tkinter.Button(root, text='Search', command=set_value_to_text)

label_top.grid(row=0, column=0)
label_prompt.grid(row=1, column=0)
label_value.grid(row=1, column=1)
label_empty_find_excel.grid(row=1, column=2)
button.grid(row=1, column=3)

label_empty1.grid(row=2, column=1)
label_ip_prompt.grid(row=3, column=1)
text_ip.grid(row=4, column=1)
label_empty2.grid(row=5, column=1)

text_result.grid(row=6, column=1)
label_empty_search.grid(row=6, column=2)
button_search.grid(row=6, column=3)

root.mainloop()
