# -*- coding: utf-8 -*-
from selenium import webdriver

browser=webdriver.Chrome()
url="https://www.zhihu.com/explore"
browser.get(url)
logo=browser.find_element_by_id("zh-top-link-logo")
print(logo)
print(logo.text)
browser.close()
