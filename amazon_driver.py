import os
import random

from requests.api import options
import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_ip():
    res = requests.get("http://api.proxy.ipidea.io/getProxyIp?num=100&return_type=json&lb=1&sb=0&flow=1&regions=&protocol=http")
    data = json.loads(res.content)
    res_list = []
    for item in data.get("data"):
        res_list.append("{}:{}".format(item.get("ip"), item.get("port")))

    return random.choices(res_list)[0]



def run():


    # --proxy-server=http://219.239.142.253:3128

    options = Options()

    # options.add_argument('--headless')
    pro = get_ip()
    print(pro)
    options.add_argument(pro)
    # UserAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    # options.add_argument('User-Agent=' + UserAgent)

    browser = webdriver.Chrome(chrome_options=options)

    url = "https://www.amazon.com"

    browser.get(url)
    browser.save_screenshot("亚马逊首页.png")


if __name__ == '__main__':
    # run()
    da = "89.32 12d"
    print(id(da))
    da = da.replace(" ","")
    print(id(da))
