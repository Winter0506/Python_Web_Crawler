import requests

# get请求获取网页源代码
r = requests.get('https://static1.scrape.cuiqingcai.com/')
print(r.text)

