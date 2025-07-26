import urllib.request

url = ('https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1740124657443_108&jsoncallback=jsonp109&action'
       '=cityAction&n_s=new&event_submit_doGetAllRegion=true')

headers = {

    # ":authority": "dianying.taobao.com",
    # ":method": "GET",
    # ":path": "/cityAction.json?activityId&_ksTS=1740120990301_116&jsoncallback=jsonp117&action=cityAction&n_s=new"
    #          "&event_submit_doGetAllRegion=true",
    # ":scheme": "https",
    "accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, "
              "*/*; q=0.01",
    # "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9",
    "bx-v": "2.5.28",
    "cookie": "cna=A4cvID17XCACASowCnpZ8GcV; t=bab4c204498638a5d021f585a583593e; "
              "cookie2=17e0fd8d55b67e6613d22d9ccfcb56fd; v=0; _tb_token_=ebe395df30153; xlly_s=1; tb_city=110100; "
              "tb_cityName=\"sbG+qQ==\"; isg=BN3d6dB6ZsSoQAL4z1N4NtvL7LnX-hFMZGDWRp-i0TRjVv2IZkuuHONIgErQoikE",
    "priority": "u=1, i",
    "referer": "https://dianying.taobao.com/?spm=a1z21.3046609.city.1.32c0112akBjqfJ&city=110100",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/133.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"

}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

content = content.split('(')[1].split(')')[0]

with open('city.json', 'w', encoding='utf-8') as fb:
    fb.write(content)

import json
import jsonpath

obj = json.load(open('city.json', 'r', encoding='utf-8'))

# print(obj)
city = jsonpath.jsonpath(obj, '$..regionName')
print(city)






