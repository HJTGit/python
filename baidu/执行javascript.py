# 下面的例子是执行就是，拖拽进度条到底，并弹出提示框

#_*_coding: utf-8_*_
import time
from selenium import webdriver
browser=webdriver.Chrome()
browser.get("https://www.zhihu.com/explore")
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
browser.execute_script("alert('To Button')")
time.sleep(5)
browser.close()
