import requests
from lxml import etree

URL = "https://www.amazon.cn/s?i=toys-and-games"


class Req:
    def __init__(self):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8`',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Cookie': 'x-wl-uid=1C5tB2vN8c7lavnzfYDgHUImOM4TnKW4RDPJRHqltEo/CzfweQDRpdn8vABF8x1AJGiV5fs7nxxs=; session-id=458-1818727-1656342; ubid-acbcn=460-9298287-9372958; session-token="qLgiMsjH5EkTiN1gyNgsmUtrW2cKLf2Y9N6fpJoYpV6d1nqVt6vvuukTz02ezeMaWJfwZGeXxoPVwGjydlOwEX1ENh0A1ZebwcEN9T69+WYA/1cV4OHxfvOPrxjIVFhMgaZqLjkHt4KZ+sGOP4gT7bAt14UlSx9tq1pyNX/8JDmQ8ouZKTL0KYAqzVA+tLgHJqlJYLNt+ovqT7ad6WamIA=="; session-id-time=2082729601l; csm-hit=tb:4DGRV0CH4S37H6HK0TQ5+s-5882EJ35HSPBDQRTWVYS|1547819207778&adb:adblk_no&t:1547818974223',
            'Connection': 'keep-alive',
            'Host': 'www.amazon.cn',
            'Referer': 'https://www.amazon.cn/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }

    def get_by_net(self, url):
        res = requests.get(url, headers=self.headers)
        print(res.text)
        html = etree.HTML(res.text)
        return html


req = Req()


def get_root_category():
    """
    获取一级类目
    :return:
    """
    html = req.get_by_net(URL)
    dt = html.xpath('//li[@class="a-spacing-micro apb-browse-refinements-indent-2"]//a[@class="a-color-base '
                    'a-link-normal"]')
    url_map = {}
    for item in dt:
        url = item.xpath("./@href")
        name = item.xpath("./span/text()")
        url_map[name[0]] = url[0]

    return url_map


def get_more(url):
    """获取更多"""
    html = req.get_by_net(url)
    hs = html.xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/a/@href")[0]
    return hs


def get_second_category(url):
    """获取二级类目"""
    html = req.get_by_net(url)
    print(html)
    # hs = html.xpath('//ul[@class="a-unordered-list a-nostyle a-vertical a-spacing-medium"]/li[@class="a-spacing-micro s-navigation-indent-2"]//a')
    hs = html.xpath('//ul[@class="a-unordered-list a-nostyle a-vertical a-spacing-medium"]/li[@class="a-spacing-micro s-navigation-indent-2"]/span/a')
    print(hs)
    url_map = {}
    for item in hs:
        url = item.xpath("./@href")
        name = item.xpath("./span/text()")
        url_map[name[0]] = url[0]
    return url_map

if __name__ == '__main__':
    uuu = "https://www.amazon.com/s?bbn=16225015011&rh=n%3A166057011&dc&qid=1660664688&rnid=16225015011&ref=lp_16225015011_nr_n_0"
    res = get_second_category(uuu)
    print(res)