import urllib.request
import urllib.parse


def create_request(page):
    url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
        "cname": "北京",
        "pid": "",
        "pageIndex": page,
        "pageSize": 10
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/132.0.0.0'
                      'Safari/537.36 Edg/132.0.0.0'
    }
    request = urllib.request.Request(url=url, data=data, headers=headers)
    return request


def get_response(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def download_file(page, content):
    with open(f'kendejiplace{page}.json', 'wt', encoding='utf-8') as file_a:
        file_a.write(content)


if __name__ == '__main__':
    start_page = int(input('请输入开始页码：'))
    end_page = int(input('请输入终止页码：'))
    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_response(request)
        download_file(page, content)