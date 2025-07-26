import urllib.request

url = 'https://user.qzone.qq.com/3520352176'
headers = {
    'cookie':
    'pgv_pvid=4195256860; ptui_loginuin=3520352176; RK=tmXs2JH68o; '
    'ptcz=1a188dfc3146bd8ebc0d3deaa3b31c0330bb27841ea6b71254b2fe229d59b894; qz_screen=1536x864; QZ_FE_WEBP_SUPPORT=1; '
    'cpu_performance_v8=0; __Q_w_s__QZN_TodoMsgCnt=1; __layoutStat=13; _qpsvr_localtk=0.9775192071518368; '
    'pgv_info=ssid=s8422231096; uin=o3520352176; skey=@pHSGm7Eo2; p_uin=o3520352176; '
    'pt4_token=trEqE*N8a4slnc2*PwTD*Y-jxGHBDK*MAULpflMQLrU_; p_skey=Py8vCP9h-BwaChjZxGuFhhJJlkUcN0Q6huBuZdsfKCg_; '
    'Loading=Yes; 3520352176_todaycount=0; 3520352176_totalcount=652',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/132.0.0.0'
                      'Safari/537.36 Edg/132.0.0.0',
    'referer':
    'https://qzs.qq.com/',
    # 'user-agent':
    # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
