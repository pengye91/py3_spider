#!/usr/bin/python3
"""author = xyp ."""
# -*- encoding: UTF-8 -*-
import urllib.request

url = "http://127.0.0.1/users"
page = urllib.request.urlopen(url)
page_data = page.read().decode("utf-8")
page_info = page.info()
page_code = page.getcode()


print(page_code)
print('----------------------------------------------------------------------')
print(page_info)
print('----------------------------------------------------------------------')
print(page_data)
