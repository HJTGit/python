# -*- coding: utf-8 -*-
from selenium import webdriver

browser=webdriver.Chrome()
url="https://www.zhihu.com/explore"
browser.get(url)
logo=browser.find_element_by_id("zh-top-link-logo")
print(logo)
#id
print(logo.id)
#位置
print(logo.location)
#标签名
print(logo.tag_name)
#大小
print(logo.size)
browser.close()
