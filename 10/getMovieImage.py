import requests
import time
from selenium import webdriver
from lxml import etree


def dowmload(name, src):
    path = "./image/video/"
    response = requests.get(src, timeout=10)
    img = open(path + name + ".jpg", "wb")
    img.write(response.content)
    img.close()


def main():
    # 下载刘亦菲电影的海报
    r = requests.get("https://www.douban.com/search?cat=1002&q=%E5%88%98%E4%BA%A6%E8%8F%B2")
    html = etree.HTML(r.text)

    path = '//div[@class="result-list"]/div[@class="result"]/div[@class="pic"]/a/img'
    res = html.xpath(path)
    titles = html.xpath(path + '/..')

    for i in zip(titles, res):
        name = i[0].get("title")
        src = i[1].get("src")
        dowmload(name, src)


def all_movie():
    chrome = webdriver.Chrome()
    chrome.get("https://www.douban.com/search?cat=1002&q=%E5%88%98%E4%BA%A6%E8%8F%B2")
    while 1:
        try:
            chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 跳转到网页底部
            time.sleep(0.5)
            more = chrome.find_element_by_xpath('//a[@class="j a_search_more"]')
            more.click()
            time.sleep(2)
        except Exception:
            print("end!")
            time.sleep(2)
            break

    print("Start download image!")
    html = etree.HTML(chrome.page_source)
    chrome.close()
    path = '//div[@class="result-list"]/div[@class="result"]/div[@class="pic"]/a/img'
    res = html.xpath(path)
    titles = html.xpath(path + '/..')

    for i in zip(titles, res):
        print(i[1].get("src"))
        name = i[0].get("title")
        src = i[1].get("src")
        dowmload(name, src)


if __name__ == '__main__':
    all_movie()
