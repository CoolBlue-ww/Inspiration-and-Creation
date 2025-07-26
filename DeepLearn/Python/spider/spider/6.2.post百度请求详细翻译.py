import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/ait/text/translate'

data = {
    "query": "man\n",
    "from": "en",
    "to": "zh",
    "reference": "",
    "corpusIds": [],
    "needPhonetic": 'true',
    "domain": "common",
    "milliTimestamp": '1739284864842'
}

data = urllib.parse.urlencode(data).encode('utf-8')

headers = {
    'Cookie': 'BIDUPSID=47FF63146438D6A2DD98E3EE2266AEC2; PSTM=1735814382; '
              'BAIDUID=47FF63146438D6A20A702D7B07FF9255:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; '
              'BAIDUID_BFESS=47FF63146438D6A20A702D7B07FF9255:FG=1; H_WISE_SIDS_BFESS=62036; '
              'ZFY=yOmtmX:BUICvIvXyhBr5Ql0sgqkSpUO9A1DkjgmG:Bf6M:C; '
              'H_PS_PSSID=60277_61027_61671_61987_62056_62061_62109_62100_62130; delPer=0; PSINO=3; '
              'H_WISE_SIDS=62036_62130; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=null; BDRCVFR['
              '-pGxjrCMryR]=mk3SLVN4HKm; BA_HECTOR=848l0l240080000gag04ak2h3e4ivi1jqmlg21v; arialoadData=false; '
              'RT="z=1&dm=baidu.com&si=c5cdc603-3ceb-4550-8190-5aae9b3ee71b&ss=m70jscyz&sl=0&tt=0&bcn=https%3A%2F'
              '%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf"; '
              'ab_sr=1.0.1_YjgxNWU1YTE3MjEyNDQxZDU5NDNkNDZjOWE5N2Q1MTIyMDAwNTEzZmUxNGIwNTA2ZmQ1ZmNiYWI5ZTAxZjU4ZTQwMDQwZTJiNzgxNmE0MjdjNjEyZDJkODFmNTc5MzE0MzAzMmM4YTk2NmMxZWRhZWQwMjRiMDM3MDY0N2ExYTc2OGJjMjFlMjEyMTZjYjkyYzhiZTFhNDM1MDM4ZDUwZA=='
}

request = urllib.request.Request(url, data, headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')
print(content)


import json

# 假设这是您从流式数据中接收到的文本
# text =
# event: message
# data: {"errno":0,"errmsg":"Success","data":{"event":"Start","message":"开始处理请求"}}
# event: message
# data: {"errno":10001,"errmsg":"Validation failed","data":null}
# event: message
# data: {"errno":0,"errmsg":"Success","data":{"event":"Finished","message":"请求处理结束"}}
# """

# 按行分割文本
lines = content.strip().split('\n')

# 遍历每一行
for line in lines:
    # 找到包含data:的部分
    if 'data:' in line:
        # 提取data后面的JSON字符串
        json_str = line.split('data: ')[1].strip()
        try:
            # 解析JSON字符串
            data = json.loads(json_str)
            print(data)
        except json.JSONDecodeError as e:
            print(f"解析错误: {e}")
