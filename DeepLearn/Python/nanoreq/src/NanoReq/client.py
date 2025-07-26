import socket
import proxy
from headers import Headers
import parse

def HttpGet(url, host, path='/', method='GET', headers=None):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(proxy.Proxy(Charles='True'))
    if proxy.Proxy(Charles='True'):
        request_line = f"{method} {url} HTTP/1.1"
    else:
        request_line = f"{method} {path} HTTP/1.1"

    headers_lines = '\r\n'.join(f"{key}: {value}" for key, value in Headers(host, headers, method).items())
    request = (request_line +
               '\r\n' +
               headers_lines +
               '\r\n\r\n'
               )
    return Request(sock, request)


def HttpPost(url, host, path='/', method='POST', headers=None, data=None):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(proxy.Proxy(Charles='True'))
    if proxy.Proxy(Charles='True'):
        request_line = f"{method} {url} HTTP/1.1"
    else:
        request_line = f"{method} {path} HTTP/1.1"

    headers, body_data = Headers(host, headers, method, data)
    headers_lines = '\r\n'.join(
        f"{key}: {value}" for key, value in headers.items())
    request = (request_line +
               '\r\n' +
               headers_lines +
               '\r\n\r\n' +
               body_data
               )
    return Request(sock, request)


def Request(sock, request):
    sock.send(request.encode())
    response = b""
    while True:
        chunk = sock.recv(10000)
        if not chunk:
            break
        else:
            response += chunk
    sock.close()
    return response


url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&fenlei=256&oq=%25E7%2599%25BE%25E5%25BA%25A6%25E7%25BF%25BB%25E8%25AF%2591&rsv_pq=cbed48b70147e9aa&rsv_t=515343PsKMVofmwh01kzVEIBgpFNzgHlocBGvTfX2KuepxBDEI8MP94yzXk&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_btype=t&inputT=7161&rsv_sug3=27&rsv_sug1=26&rsv_sug7=101&rsv_sug2=0&rsv_sug4=7161&rsv_sug=1'
a = parse.SplitUrl(url)

host = a['host']
path = a['path']
headers = Headers(host, a, 'GET', path)
data = HttpGet(url, host, path, 'GET', headers)
print(data)

