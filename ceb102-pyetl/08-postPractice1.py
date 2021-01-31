import requests

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': '123123123123vchjzvhxjckzvhcjzhvcxljkz'
}
data = {
    'key1': 'value1',
    'key2': 'value2'
}

res = requests.post(url, data=data, headers=headers)

# print(res.text)

url = 'http://e2c30d442303.ngrok.io/hello_post'
data = {
    'username': 'vhcjzHCjxkzlHCjxkzl'
}
res = requests.post(url, data=data)
print(res.text)