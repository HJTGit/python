# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException

browser=webdriver.Chrome()
try:
    browser.get("https://www.zhihu.com/explore")
except TimeoutException:
    print("Time out")
try:
    browser.find_element_by_id("hello")
except NoSuchElementException:
    print("No Element")
finally:
    browser.close()
