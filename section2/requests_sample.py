import requests

s = requests.Session()
s.headers.update({'user-agent': 'my-crawler/1.0 (+foo@example.com)'})

# r = requests.get('http://weather.livedoor.com/forecast/webservice/json/v1?city=130010')
# print(r.json())

r = s.get('http://weather.livedoor.com/forecast/webservice/json/v1?city=130010')
# r = s.get('https://gihyo.jp/dp')
print(r.headers)