# 请求对象的定制
import urllib.request

# url的组成
# url = 'http://www.baidu.com'
# http/https      www.baidu.com    80/443        s       wd=周杰伦    #
#    协议                主机        端口号        路径        参数     锚点

headers = {
'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0'
}

url = 'https://www.baidu.com'
# 请求对象的定制
# 因为变量顺序问题，所以录入变量时，要使用关键字传参
request = urllib.request.Request(url=url, headers=headers)  # 因为open方法不能写入字典，所以需要建立一个request对象
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
