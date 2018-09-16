#!/usr/bin/python
# coding: utf-8
import uuid

def get_mac_address():
    node = uuid.getnode()
    mac = uuid.UUID(int = node).hex[-12:]
    return mac

a = get_mac_address()
print(a)
