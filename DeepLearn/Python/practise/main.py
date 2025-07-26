import requests
from lxml import etree

# 需要获取的网站地址
URL = 'https://www.hongxiu.com/chapter/28355038604534004/76130172289477040'

source_code = requests.get(URL).text

# 打印网页源代码print(source_code)
# 对网页源代码进行解析
data = etree.HTML(source_code)
"""
打印解析的数据
print(data)
"""
# 查找数据中的文章
content = data.xpath('//*[@id="chapter-76130172289477040"]/div/div[2]/div/p')
# 打印找到的<p>标签print(content)
# 建立一个存放文章的文件
file = open('外太空传说第一章.text', 'wt', encoding='utf-8')

for p in content:
    print(p)
    file.write(p.text + "\n")
