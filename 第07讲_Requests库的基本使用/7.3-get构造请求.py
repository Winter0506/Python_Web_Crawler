import requests

data = {
    'name':'xiaowang',
    'age':25
}

r = requests.get('http://httpbin.org/get',params=data)
print(r.text)