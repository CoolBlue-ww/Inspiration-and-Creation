import requests
from bs4 import BeautifulSoup


# 登录页面的地址链接
url = 'https://www.gushiwen.cn/user/login.aspx?from=http://www.gushiwen.cn/user/collect.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 '
                  'Safari/537.36'
}
# 向服务器发送请求获取响应
response = requests.get(url=url, headers=headers)
# 获取网页源码
content = response.text
# 获取页面中的隐藏域信息
soup = BeautifulSoup(content, 'lxml')
viewstate = soup.select('#__VIEWSTATE')[0]['value']
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0]['value']

# 获取网页中的验证码信息
img_url = 'https://www.gushiwen.cn' + soup.select('#imgCode')[0]['src']
# 创建一个session对象
session = requests.session()
img_data = session.get(img_url)
with open('img_data.jpg', 'wb') as fb:
    fb.write(img_data.content)

code = input("请输入验证码：")

# 传递参数
data = {
    "__VIEWSTATE": viewstate,
    "__VIEWSTATEGENERATOR": viewstategenerator,
    "from": "http://www.gushiwen.cn/user/collect.aspx",
    "email": "3520352176@qq.com",
    "pwd": "COOKIE",
    "code": code,
    "denglu": "登录"
}
# 模拟登录
response = session.post(url=url, headers=headers, data=data)

content = response.text
print(content)
