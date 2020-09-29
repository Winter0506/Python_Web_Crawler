import requests
import re

data = {
    'name':'xiaowang',
    'age':25
}

r = requests.get('http://httpbin.org/get',params=data)
print(r.text)

r1 = requests.get('http://httpbin.org/get')
print(type(r1.text))
print(r1.json())
print(type(r1.json()))
'''
<class 'str'>
{'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.24.0', 'X-Amzn-Trace-Id': 'Root=1-5f73368e-004da00b03cc3c533d0715b9'}, 'origin': '112.10.180.218', 'url': 'http://httpbin.org/get'}
<class 'dict'>
'''

# 抓取网页

r2 = requests.get('https://static1.scrape.cuiqingcai.com/')
pattern = re.compile('<h2.*?>(.*?)</h2>',re.S)
titles = re.findall(pattern,r2.text)
print(titles)
'''
['霸王别姬 - Farewell My Concubine', '这个杀手不太冷 - Léon', '肖申克的救赎 - The Shawshank Redemption', '泰坦尼克号 - Titanic', '罗马假日 - Roman Holiday', '唐伯虎点秋香 - Flirting Scholar', '乱世佳人 - Gone with the Wind', '喜剧之王 - The King of Comedy', '楚门的世界 - The Truman Show', '狮子王 - The Lion King']
'''

# 抓取二进制数据

r3 = requests.get("https://github.com/favicon.ico")
print(r3.text)
print(r3.content)

with open('favicon.ico','wb') as f:
    f.write(r.content)

