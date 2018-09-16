#!/usr/bin/python
# coding: utf-8

from cookie import CookieJar
import urllib2
import urllib
import json


def get_info():
    cj = CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    data_encoded = urllib.urlencode(form_data_dict)

    opener.open(url_login, data_encoded)
    response = opener.open(url_info)

    content = json.loads(response.read())

    # return dict
    return content


def main():
    get_inf()


if __name__ == "__main__":
    main()
