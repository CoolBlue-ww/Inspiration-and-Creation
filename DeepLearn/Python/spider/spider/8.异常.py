import urllib.request
import urllib.error

url = 'https://blog.cnet/qq_74232707/article/details/14494552'

try:
    response = urllib.request.urlopen(url)

    content = response.read().decode('utf-8')

    print(content)
except urllib.error.HTTPError:
    print('正在升级')
except urllib.error.URLError:
    print('正在修正')
