import urllib.request
import urllib.parse


def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&'
    data = {
        'start': (page - 1) * 20,
        'limit': 20
    }
    # import urllib.parse
    data = urllib.parse.urlencode(data)
    url = base_url + data
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/132.0.0.0'
                      'Safari/537.36 Edg/132.0.0.0'
    }
    # import urllib.request
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    # import urllib.request
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def download_file(page, content):
    with open('douban' + str(page) + '.json', 'wt', encoding='utf-8') as file:
        file.write(content)


if __name__ == '__main__':
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入终止页码：'))
    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        download_file(page, content)
