# _*_coding: utf-8_*_

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://www.taobao.com")
lis = browser.find_element_by_css_selector("li")
lis_c = browser.find_element(By.CSS_SELECTOR, "li")
print(lis)
print(lis_c)
browser.close()
