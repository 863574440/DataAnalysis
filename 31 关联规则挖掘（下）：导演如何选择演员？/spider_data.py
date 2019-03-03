from splinter.browser import Browser
import csv
import time
from splinter.exceptions import ElementDoesNotExist


def download_data(url):
    director = "张艺谋"
    file_name = './data/data.csv'
    out = open(file_name, "w", encoding='utf-8')
    csv_writer = csv.writer(out, dialect="excel")

    chrome = Browser("chrome")
    chrome.visit(url)

    while 1:
        movie_list = chrome.find_by_xpath(
            '//div[@class="item-root"]//div[@class="detail"]//div[@class="title"]//a')
        name_list = chrome.find_by_xpath(
            '//div[@class="item-root"]//div[@class="detail"]/div[@class="meta abstract_2"]')
        num = len(movie_list)
        if num > 15:  # 第一页会有 16 条数据
            # 默认第一个不是，所以需要去掉
            movie_list = list(movie_list)[1:]
            name_list = list(name_list)[1:]

        for movie_name, names in zip(movie_list, name_list):
            # 会存在数据为空的情况
            if names.text is None:
                continue
            # 显示下演员名称
            print(names.text)
            names = names.text.split('/')
            # 判断导演是否为指定的 director
            if names[0].strip() == director:
                # 将第一个字段设置为电影名称
                names[0] = movie_name.text
                csv_writer.writerow(names)
        time.sleep(1)
        try:
            chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            bttn = chrome.find_by_xpath('//a[@class="next"]')
            bttn[0].click()
        except ElementDoesNotExist:
            break
    chrome.quit()


def main():
    url = 'https://movie.douban.com/subject_search?search_text=%E5%BC%A0%E8%89%BA%E8%B0%8B&cat=1002'
    download_data(url)


if __name__ == '__main__':
    main()
