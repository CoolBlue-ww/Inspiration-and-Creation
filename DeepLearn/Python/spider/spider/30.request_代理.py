import requests
import random

url = 'https://www.baidu.com/s?'

headers = {
    "accept": "*/*",
    "is_referer": "https://www.baidu.com/",
    "is_xhr": "1",
    "ps-dataurlconfigqid": "0xa22a78f1031e4eb4",
    "referer": "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=IP&fenlei=256&rsv_pq=0xa22a78f1031e4eb4&rsv_t=6d13TOPikjON3SsLgy6LosRkLxDN4lT7VHP9dBU4znD23YqvHE2Nme5LPDe3&rqlang=en&rsv_dl=tb&rsv_enter=1&rsv_sug3=4&rsv_sug1=4&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&prefixsug=IP&rsp=5&inputT=7257&rsv_sug4=7257",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

data = {
    'wd': 'ip'
}

proxy = [
    {'http': '167.172.6.236:3128'},
    {'http': '177.234.196.21:999'},
    {'http': '103.84.177.215:8082'},
    {'http': '103.167.222.19:8181'}
]

proxy = random.choice(proxy)

response = requests.get(url=url, data=data, headers=headers, proxies=proxy)

response.encoding = 'utf-8'

content = response.text

with open('ip.html', 'w', encoding='utf-8') as fb:
    fb.write(content)
