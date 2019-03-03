from splinter.browser import Browser
import requests
import re
import pandas as pd
import time
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/71.0.3578.98 Safari/537.36"}


def get_data():
    page_index = 1
    movie_links = {"电影名": [], "迅雷下载链接": []}
    chrome = Browser("chrome")
    chrome.visit("https://www.dy2018.com/html/gndy/dyzz/index.html")

    while 1:
        print("page", page_index)
        try:
            links = chrome.find_by_xpath('//a[@class="ulink"]')
        except Exception:
            links = None

        chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 跳转到页面底部

        for link in links:
            href = link["href"]
            movie_name = link.text  # 获取电影名

            # 截取电影名
            try:
                sub_movie_name = movie_name[(movie_name.index("《")): (movie_name.index("》") + 1)]
            except ValueError:
                sub_movie_name = movie_name
            movie_links["电影名"].append(sub_movie_name)

            # 获取电影详情页面
            try:
                response = requests.get(href, headers=headers)
                response.encoding = "gb2312"
                html = response.text
                html.encode("utf-8")
            except requests.exceptions.ConnectionError:
                print("获取网页错误！", end=": ")
                html = "null"

            # 获取下载链接
            # try:
            #     pattern = re.compile('>(ftp://.+)</a>')
            #     match = pattern.search(html).group(1)
            # except Exception:
            #     try:
            #         pattern = re.compile('<a href="(ftp://.+)">(.+)</a>')
            #         match = pattern.search(html).group(2)
            #     except AttributeError as e:
            #         print(str(e), end=":")
            #         match = "获取下载链接失败！"

            try:
                etree_html = etree.HTML(html)
                hrefs = etree_html.xpath("//td//a//text()")
                if len(hrefs) == 0:
                    raise Exception
                download_link = hrefs[0]
            except Exception:
                download_link = "获取下载链接失败！"

            movie_links["迅雷下载链接"].append(download_link)
            print(sub_movie_name, ":", download_link)  # 打印电影名和下载链接

        time.sleep(1)
        try:  # 点击下一页
            next_page = chrome.find_by_text("下一页")
            next_page[0].click()
            page_index += 1
        except Exception:
            print("All movies have been got!")
            return movie_links


def write_to_excel(movies):
    print("正在保存...")
    dataframe = pd.DataFrame(movies)
    dataframe.to_excel("./data/movies2.xlsx")
    print("保存成功！")


def main():
    movies = get_data()
    write_to_excel(movies)


if __name__ == '__main__':
    main()
