def Headers(host, headers=None, method='GET', data=None):
    headers = headers or {}
    headers['Accept'] = headers.get('Accept',
                                    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7')
    headers['Accept-Encoding'] = headers.get('Accept-Encoding', 'gzip, deflate, br, zstd')
    headers['Accept-Language'] = headers.get('Accept-Language', 'zh-CN,zh;q=0.9,en;q=0.8')
    headers['Cache-Control'] = headers.get('Cache-Control', 'no-cache')
    headers['Connection'] = headers.get('Connection', 'close')
    headers['Cookie'] = headers.get('Cookie', '')
    headers['Host'] = headers.get('Host', host)
    headers['Pragma'] = headers.get('Pragma', 'no-cache')
    headers['Referer'] = headers.get('Referer', 'https://www.google.com')
    headers['Sec-Ch-Ua'] = headers.get('Sec-Ch-Ua', '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"')
    headers['Sec-Ch-Ua-Mobile'] = headers.get('Sec-Ch-Ua-Mobile', '?0')
    headers['Sec-Ch-Ua-Platform'] = headers.get('Sec-Ch-Ua-Platform', 'Windows')
    headers['Sec-Fetch-Dest'] = headers.get('Sec-Fetch-Dest', 'document')
    headers['Sec-Fetch-Mode'] = headers.get('Sec-Fetch-Mode', 'navigate')
    headers['Sec-Fetch-Site'] = headers.get('Sec-Fetch-Site', 'same-origin')
    headers['Sec-Fetch-User'] = headers.get('Sec-Fetch-User', '?1')
    headers['Upgrade-Insecure-Requests'] = headers.get('Upgrade-Insecure-Request', '1')
    headers[
        'User-Agent'] = headers.get('User-Agent',
                                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36')
    if method == 'POST':
        body_data = ""
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        if isinstance(data, dict):
            body_data = '&'.join(f"{key}: {value}" for key, value in data.items())
            body_data_len = str(len(body_data.encode('utf-8')))
            headers['Content-Length'] = body_data_len
            return headers, body_data
        else:
            raise TypeError('Data must be dict.')
    else:
        return headers
