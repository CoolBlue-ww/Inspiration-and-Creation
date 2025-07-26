import requests

url = 'https://fanyi.baidu.com/sug'

headers = {
    "accept": "*/*",
    # "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9",
    "connection": "keep-alive",
    "content-length": "6",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": "BIDUPSID=F147422086959B41C0300BA14A81A073; PSTM=1740558654; BAIDUID=F147422086959B41C0300BA14A81A073:FG=1; BAIDUID_BFESS=F147422086959B41C0300BA14A81A073:FG=1; H_PS_PSSID=60275_61027_61671_62067_62130_62127_62168_62185_62186_62182_62196_62232_62305_62134_62325; BA_HECTOR=2h81a1252580aha0808001819tgft41js24t71v; ZFY=8oCprr0:BvoZXQlulEkQG6ie4KdBhG74plCyjfKWBd:AU:C; PSINO=3; delPer=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BCLID=5091926702567143000; BCLID_BFESS=5091926702567143000; BDSFRCVID=OrKOJexroGWIeXOJkj-yEHtYoFweG7bTDYrEOwXPsp3LGJLVvqHuEG0Pts1-dEu-S2OOogKKLmOTHprwc2L2Ay_P_VWs7Wn7dHrytf8g0M5; BDSFRCVID_BFESS=OrKOJexroGWIeXOJkj-yEHtYoFweG7bTDYrEOwXPsp3LGJLVvqHuEG0Pts1-dEu-S2OOogKKLmOTHprwc2L2Ay_P_VWs7Wn7dHrytf8g0M5; H_BDCLCKID_SF=tRAOoC_-tDvDqTrP-trf5DCShUFs047JB2Q-XPoO3M3zefnOy4R8XxCkyhOk2M5f5mkf3fbgy4op8P3y0bb2DUA1y4vp-Jo7bmTxoUJ2-KDVeh5Gqq-KXU4ebPRiWPr9QgbjQt3Jtq4KEtT30hn43nJW3UIfKUvHM6nhVn0MBCK0hD89DjKKD6PVKgTa54cbb4o2WbCQBpor8pcN2b5oQp-PbJ79BtnBBjQ4aPbwahQbeq06-lOUWJDkXpJvQnJjt2JxaqRCbtj1fq5jDh3MKToDb-oteltHB2Oy0hvcBn6cShnxKRJjDx7XLqrdQpRpQ5Af-bu55pnKJtbIe-t2XjQhDH-OJ6DHtJ3h3RrX26rDHJTg5DTjhPrMDPRdWMT-MTryKM3Y5xncORvFXR6pyb04hPjfKx-fKHnRh4oNbpRDhx5J0POaL60Z5lQ7-xQxtNRJQKDE5p5hKf84XUnobUPUXMc9LUvj-jv2oq4-04TrVM7K3n-b3P6Wb-7HhR3hfIkj2CKLtC8WhD_4D6RDKICV-frb-C62aKDs2-ocBhcqJ-ovQpJzbqkgyxRBeRc4WTnkWhQ55l0bHxbeWJ5pXn-R0hbjJM7xWeJpLtjdbl5nhMJmKTLVbML0qJ-HWMRy523i2n6vQpn2q43nDxkKLJFm0bnpLbtfQK_f0pn-M4btbb0xXj_0-nDSHHLDJ5DD3H; H_BDCLCKID_SF_BFESS=tRAOoC_-tDvDqTrP-trf5DCShUFs047JB2Q-XPoO3M3zefnOy4R8XxCkyhOk2M5f5mkf3fbgy4op8P3y0bb2DUA1y4vp-Jo7bmTxoUJ2-KDVeh5Gqq-KXU4ebPRiWPr9QgbjQt3Jtq4KEtT30hn43nJW3UIfKUvHM6nhVn0MBCK0hD89DjKKD6PVKgTa54cbb4o2WbCQBpor8pcN2b5oQp-PbJ79BtnBBjQ4aPbwahQbeq06-lOUWJDkXpJvQnJjt2JxaqRCbtj1fq5jDh3MKToDb-oteltHB2Oy0hvcBn6cShnxKRJjDx7XLqrdQpRpQ5Af-bu55pnKJtbIe-t2XjQhDH-OJ6DHtJ3h3RrX26rDHJTg5DTjhPrMDPRdWMT-MTryKM3Y5xncORvFXR6pyb04hPjfKx-fKHnRh4oNbpRDhx5J0POaL60Z5lQ7-xQxtNRJQKDE5p5hKf84XUnobUPUXMc9LUvj-jv2oq4-04TrVM7K3n-b3P6Wb-7HhR3hfIkj2CKLtC8WhD_4D6RDKICV-frb-C62aKDs2-ocBhcqJ-ovQpJzbqkgyxRBeRc4WTnkWhQ55l0bHxbeWJ5pXn-R0hbjJM7xWeJpLtjdbl5nhMJmKTLVbML0qJ-HWMRy523i2n6vQpn2q43nDxkKLJFm0bnpLbtfQK_f0pn-M4btbb0xXj_0-nDSHHLDJ5DD3H; ab_sr=1.0.1_YjAzZGVlNDAyZjc4YzM2NTI5ODkzMGY1ZDM1MzhkMTE4NDYzOTQ0ZGVhNjgxNzAxMTE1MDAzNWQyZTBlYjgyYjNkMjE0YWEzZDkzNTdlMDIyN2QxMzUzYWVmYWE0ODRmMDc1NjZlMzY4NmIwYjg4YWVjN2E3ODRlNzFlYmUxMGJjZDFhZjlmMjY3MTQxOTZmZjg5NjdlZjdlYjJhNzgwNGMzNGZiOThkNWQ5OGNlODE2MzE2ZWUzMDYzODE4NTZiZjlhZjcyNGUwYmM5YjlkYzkyN2UzYTY1NzZiYjlmOTE=; RT=\"z=1&dm=baidu.com&si=9bc40451-b615-496e-95c9-bd3873c31d01&ss=m7o4i697&sl=a&tt=cm9&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=bi8e\"",
    "host": "fanyi.baidu.com",
    "origin": "https://fanyi.baidu.com",
    "referer": "https://fanyi.baidu.com/mtpe-individual/multimodal?query=m&lang=en2zh&ext_channel=Aldtype",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}

data = {
    'kw': 'man'
}

response = requests.post(url=url, data=data, headers=headers)

response.encoding = 'utf-8'

content = response.text

print(content)

import json

obj = json.loads(content, encoding='utf-8')
print(obj)
