import requests

url = 'https://msedgedriver.crosoft.com/138.0.51.121/edgedriver_win64.zip'
resp_head = requests.head(url, allow_redirects=True)
print(resp_head.status_code)



