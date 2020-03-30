import requests
import json

target_url = 'https://www.bbc.com/zhongwen/simp/world-51869081'
url = f'http://127.0.0.1:8000/gne'
resp_html = requests.get(target_url).text
resp = requests.post(url, data=json.dumps({'html': resp_html, 'url': target_url}))
print(resp.text)