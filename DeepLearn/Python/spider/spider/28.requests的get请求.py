import requests

url = 'https://www.baidu.com/s'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 '
                  'Safari/537.36'
}

data = {
    'wd': '周杰伦'
}

response = requests.get(url=url, params=data, headers=headers)

response.encoding = 'utf-8'

content = response.text

print(content)
