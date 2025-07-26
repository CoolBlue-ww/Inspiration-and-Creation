import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/sug'
data = {
    'kw': 'man'
}
new_data = urllib.parse.urlencode(data).encode('utf-8')

headers = {
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 '
        'Safari/537.36 Edg/132.0.0.0'
}

request = urllib.request.Request(url, new_data, headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)

import json

data = json.loads(content)
print(data['data'][0]['v'])

