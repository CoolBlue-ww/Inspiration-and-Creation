import socket
import time
import random


def send_http_via_proxy():
    # 连接到 Charles 代理
    sock = socket.socket()
    sock.connect(("127.0.0.1", 8888))  # Charles 代理地址

    # 构造符合规范的 HTTP 请求
    headers = {
        "Host": "www.baidu.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "close",
        "Referer": "https://www.google.com/",
    }
    request_lines = [f"{key}: {value}" for key, value in headers.items()]
    request = (
            "GET http://baidu.com HTTP/1.1\r\n"  # 注意完整 URL
            + "\r\n".join(request_lines)
            + "\r\n\r\n"
    ).encode()

    sock.send(request)

    # 读取响应
    response = b""
    while True:
        chunk = sock.recv(4096)
        if not chunk:
            break
        response += chunk
    print(response.decode())

    sock.close()


# 随机延迟后发送请求
time.sleep(random.uniform(1, 3))
print(send_http_via_proxy())
