import requests
from bs4 import BeautifulSoup

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
headers = {
    'User-Agent': userAgent
}
url = 'https://www.ptt.cc/bbs/joke/index.html'

# req = request.Request(url=url, headers=headers)
# res = request.urlopen(req)
# html = res.read().decode('utf-8')

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')
print(soup)
