import requests
from lxml import etree
# import pandas as pd
import time
import re

# import openpyxl
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 启动并初始化webdriver
options = webdriver.ChromeOptions()  # 初始化Chrome
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("disable-web-security")
options.add_argument('disable-infobars')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(chrome_options=options)
wait = WebDriverWait(driver, 20)

driver.maximize_window()

search_page_url = 'https://www.amazon.com'
postal = "20237"  # 华盛顿
print("正在爬取初始页面", search_page_url)
try:
    driver.get(search_page_url)
except Exception as e:
	driver.quit()
	print (e)
	raise  # raise语句也可以不带参数，此时按原错误信息抛出。//raise MyError('invalid value: %s' % s)
time.sleep(2)

#
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-result-list")))
