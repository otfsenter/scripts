#!/usr/bin/python

import itchat


def send_move():
    users = itchat.search_friends(name='jianhong_wu')
    print(users)
    user_name = users[0]['UserName']
    itchat.send("just do it", toUserName=user_name)
    print('succeed')


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    send_move()
