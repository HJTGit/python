# -*- coding: utf-8 -*-
from selenium import webdriver
import time

browser=webdriver.Chrome()
browser.get("https://www.taobao.com")
browser.get("https://www.test.com")
browser.get("https://www.jd.com")
browser.back()
time.sleep(1)
browser.forward()
browser.close()
