#!/bin/python
# _*_ coding: utf-8 _*_
# @Author   : otfsenter
import json
from pprint import pprint

import requests

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


def delete_server():
    order = input("Please input your order: ")
    url_item = url_root + order + '/'
    status_code = requests.delete(url_item).status_code
    pprint(get_server())
    print(status_code)


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
            return str(index), schedule

    if now_name not in names:
        return None, None


def get_now():
    name = input('Please input your name: ')
    schedule = input('Please input your schedule: ')
    c = {"name": name, "schedule": schedule}
    return c


def update_post():
    pprint(get_server())

    now_dict = get_now()
    now_name = now_dict.get('name', None)
    now_schedule = now_dict.get('schedule', None)

    server_index, server_schedule = parse_server(now_name)

    if now_schedule and now_name:
        if server_index:
            url_item = url_root + server_index + '/'
            if now_schedule != server_schedule:
                code_update = update_server(url_item, now_dict)
                if not code_update.startswith('2'):
                    print('network is bad')
        elif 's' in now_schedule and 'e' in now_schedule:
            code_post = post_server(url_root, now_dict)
            if not code_post.startswith('2'):
                print('network is bad')
    pprint(get_server())


def start():
    pprint(get_server())
    flag = input("1) Update or Post: \n2) Delete: \n")
    if flag == '1':
        update_post()
    elif flag == '2':
        delete_server()


def main():
    start()


if __name__ == '__main__':
    main()
