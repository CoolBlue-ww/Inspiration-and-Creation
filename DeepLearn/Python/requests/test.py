import requests
from lxml import etree
import time


url = 'https://sc.chinaz.com/tupian/renwutupian.html'
xpath = "//div/div[contains(@class, 'tupian-list')]/div[contains(@class, 'item')]/img/@alt"
start = time.time()
response = requests.get(url)
response.encoding = 'utf-8'
content = response.text
tree = etree.HTML(content)
alt_list = tree.xpath(xpath)
print(len(alt_list))
for alt in alt_list:
    content = requests.get(f"http://127.0.0.1:8000/extract_keywords?text={alt}").text
    print(content)
end_time = time.time()
print(f"耗时：{end_time - start}秒")
