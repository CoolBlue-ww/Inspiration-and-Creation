# 编解码
# get的请求方法
# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
import urllib.request
import urllib.parse

url = 'https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6'
headers = {
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 '
        'Edg/132.0.0.0'
}

# 将周杰伦变成Unicode编码
# name = urllib.parse.quote('周杰伦')
print(url)
# request = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(request)
#
# # 获取响应的内容
# content = response.read().decode('utf-8')
#
# # 打印数据
# # print(content)
