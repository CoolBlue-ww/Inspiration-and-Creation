import requests
import random
import time
import tqdm
from fake_useragent import UserAgent
from lxml import etree

# headers
user_agent = UserAgent()
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    # 接收的文件类型
    "accept-encoding": "gzip, deflate, br, zstd",  # * identity compress  压缩方式
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",  # 语言偏好
    "cache-control": "max-age=0",  # 指示缓存行为  max-age= 期望响应年龄不大于指定秒数， max-stale= 愿意接受过期时间不超过指定秒数的陈旧响应， min-fresh= 要求响应在接下来指定秒数内保持新鲜， no-cache 不直接禁用缓存，而是要求在使用缓存副本之前，必须向源服务器重新验证其有效性， no-store 真正禁用任何缓存存储请求和响应的任何部分， no-transform 禁止代理修改响应内容， only-if-cached 只从缓存获取响应，不查询源服务器（缓存未命中则返回504）。
    "connection": "keep-alive",  # close Upgrade  连接
    "cookie": None,  # cookie 维持会话状态，用户偏好
    "content-type": None,  # application/json application/x-www-form-urlencoded multipart/form-data;boundary=----WebKitFormBoundary7MA4YWxkTrZuOgW text/plain;charset=UTF-8 指定请求体的MIME类型
    "content-length": None,  # 指明请求体大小
    "authorization": None,  # 向服务器提供用户代理的身份凭据，用于访问受保护的内容
    "if-modified-since": None,  # 与last-modified响应头配合使用，请求服务器，如果资源在指定日期（HTTP日期时间戳）之后没有被修改过返回 304 Not Modified（空响应体），否则返回完整的资源。用于缓存验证。
    "if-none-match": None,  # 与etag响应头配合使用。请求服务器：如果资源的etag与提供的任何一个值（逗号分隔etag值列表（带引号），*匹配任何存在的资源）都不匹配（即资源已改变），则返回完整的资源；否则返回 304 Not Modified。用于缓存验证，比if-modified-since更精准
    "if-match": None,
    "if-unmodified-since": None,
    "host": None,  # 主机名
    "referer": None,  # 源链接
    "origin": None,  # 来源URL（无路径） 在跨域请求中，标明请求来源
    "pragma": "no-cache",  # 已经被弃用，仅no-cache有效能够禁用缓存
    "priority": "u=1, i",  # 优先级（firefox）
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",  # 列出浏览器品牌及重要版本，逗号分隔不同版本
    "sec-ch-ua-full-version-list": None,  # 提供浏览器品牌的完整版本信息
    "sec-ch-ua-mobile": "?0",  # ?0 不是移动设备 ?1 是移动设备
    "sec-ch-ua-platform": "\"Windows\"",  # Windows Linux IOS Android macOS声明客户端操作系统或平台
    "sec-fetch-dest": "document",  # audio 音频资源 document 主文档 embed 嵌入资源 empty 无明确类型 font 字体文件 image 图片资源 manifest WebAppManifest object 对象资源 script JavaScript脚本 style CSS样式表 track 媒体字幕 video 视频资源 worker WebWorker脚本 xslt XSLT转换文件 请求的目标资源类型
    "sec-fetch-mode": "navigate",  # cors 跨域请求，要求服务器返回有效CORS（跨域资源共享）响应头 no-cors 跨域请求但不要求CORS头，响应受限制（不能读取完整内容） same-origin 仅允许同源请求，跨域请求会被浏览器拦截 navigate 页面导航请求（如点击链接，表单提交） websocket WebSocket连接请求
    "sec-fetch-site": "cross-site",  # same-origin 请求来源页面与目标资源完全同源 same-site 来源与目标属于同一站点(a.demo.com与b.demo.com) cross-site 来源与目标跨站点 none 请求无关联页面来源（如直接地址栏输入、书签打开、重定向)
    "sec-fetch-user": "?1",  # ?1 表示是用户主动触发  ?0 表示非用户主动触发
    "upgrade-insecure-requests": "1",  # 客户端向服务器表明它更倾向于使用HTTPS加载资源。服务器据此重定向到HTTPS或设置HSTS头
    "dnt": None,  # 1 表示用户不希望被跟踪 0 表示用户希望被跟踪
    "x-forwarded-for": None,  # 以逗号分隔的IP地址列表 用于标识原始客户端地址，最左边是原始客户端IP，后续是经过的每个代理的IP
    "x-requested-with": None,  # XMLHttpRequest 常用于标识是否由AJAX调发引起
    "range": None,  # bytes=范围 请求服务器返回资源的指定部分（字节范围），用于断点续传、分块下载等。（0-22， -500， 884-）
    "user-agent": user_agent.random
}
edge_headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
}

chrome_headers = {
    "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}

firefox_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0"
}

linux_edge_headers = {
    "sec-ch-ua-platform": "\"Linux\"",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
}

linux_chrome_headers = {
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

linux_firefox_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
}

re_ = {
    'User-Agent': 'python-requests/2.31.0',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*', 'Connection': 'keep-alive'
}

a = time.time()
response = requests.get(url="https://www.runoob.com/python3/python3-examples.html")
b = time.time()
xpath = "//div/div[contains(@class, 'tupian-list')]/div[contains(@class, 'item')]/img/@alt"
response.encoding = 'utf-8'
content = response.text
c = time.time()
tree = etree.HTML(content)
alt_list = tree.xpath(xpath)
d = time.time()
print(content)
print((b - a) * 1000)
print(alt_list)
print((d - c) * 1000)
