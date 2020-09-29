'''
这里分别打印输出 status_code 属性得到状态码，
输出 headers 属性得到响应头，
输出 cookies 属性得到 Cookies，
输出 url 属性得到 URL，
输出 history 属性得到请求历史。
'''

import requests

r = requests.get('https://static1.scrape.cuiqingcai.com')
print(type(r.status_code),r.status_code)
print(type(r.headers),r.headers)
print(type(r.cookies),r.cookies)
print(type(r.url),r.url)
print(type(r.history),r.history)