import urllib.request
import random

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/132.0.0.0'
                  'Safari/537.36 Edg/132.0.0.0'
}

request = urllib.request.Request(url=url, headers=headers)

proxies_pool = [
    {'http': '149.135.910'},
    {'http': '173.378.222'}
]

proxies = random.choice(proxies_pool)

# print(proxies)
handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

with open('ip2.html', 'w', encoding='utf-8') as fb:
    fb.write(content)
