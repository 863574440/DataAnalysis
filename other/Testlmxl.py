from lxml import etree
import requests

l = requests.get('https://www.dy2018.com/html/gndy/dyzz/20130119/41194.html')
l.encoding = 'gb2312'
html = l.text
html.encode('utf-8')

et = etree.HTML(html)
lins = et.xpath('//td//a//text()')
print(lins[0])
print(html)


# from lxml import etree
#
# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
#  </div>
# '''
# html = etree.HTML(text)
# s = html.xpath('//li//text()')
# # print(etree.tostring(s[0]))
# print(s[0])
