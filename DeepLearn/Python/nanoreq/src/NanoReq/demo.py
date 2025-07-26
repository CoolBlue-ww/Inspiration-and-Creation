import socket
import urllib.parse


def send_http_request(host, port=80, path='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&fenlei=256&oq=%25E7%2599%25BE%25E5%25BA%25A6%25E7%25BF%25BB%25E8%25AF%2591&rsv_pq=cbed48b70147e9aa&rsv_t=515343PsKMVofmwh01kzVEIBgpFNzgHlocBGvTfX2KuepxBDEI8MP94yzXk&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_btype=t&inputT=7161&rsv_sug3=27&rsv_sug1=26&rsv_sug7=101&rsv_sug2=0&rsv_sug4=7161&rsv_sug=1', method="GET", headers=None, body=None):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        print("Charles连接成功！")
    except socket.error as e:
        print(str(e))

    request_line = f"{method} {path} HTTP/1.1"
    headers = headers or {}
    # headers["Host"] = headers.get("Host", host)
    headers["Host"] = "www.baidu.com"
    headers["Connection"] = "close"
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    headers["User-Aegrt"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
    headers_lines = "\r\n".join(f"{k}: {v}" for k, v in headers.items())

    body_data = ""
    if body:
        if isinstance(body, dict):
            body_data = "&".join(f"{k}: {v}" for k, v in body.items())
            headers["Content-Type"] = "application/x-www-form-urlencoded"
        headers["Content-Length"] = str(len(body_data.encode("utf-8")))

    request = (
            request_line +
            "\r\n" +
            headers_lines +
            "\r\n\r\n" +
            body_data
    )
    s.send(request.encode())

    response = b""
    while True:
        chunk = s.recv(10000000)
        if not chunk:
            break
        response += chunk

    s.close()
    return response.decode()


print(send_http_request(host="127.0.0.1", port=8888))

# print(send_http_request(
#     host="httpbin.org",
#     path="/post",
#     method="POST",
#     body={
#         "key": "value"
#     }
# ))

# import requests
#
# content = requests.post(url='https://fanyi.baidu.com/sug', data=
# {'kw': '你好'},
#                         headers={
#                             "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
#                         }).text
# print(content)
