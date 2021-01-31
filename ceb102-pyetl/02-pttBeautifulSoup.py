from urllib import request
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
headers = {
    'User-Agent': userAgent
}
url = 'https://www.ptt.cc/bbs/joke/index.html'

req = request.Request(url=url, headers=headers)
res = request.urlopen(req)
html = res.read().decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')
# print(soup)
# print(type(soup))

# logo = soup.findAll('a', {'id': 'logo'})
logo = soup.findAll('a', id='logo')
print(logo[0])
# print(type(logo[0]))

print(logo[0].text)
print('https://www.ptt.cc' + logo[0]['href'])

bbsContent = soup.findAll('div', class_='bbs-content')
print('====')
print(bbsContent[0])
print('====')
print(bbsContent[0].findAll('div'))
print('====')
print(bbsContent[0].findAll('a'))

######################

print('============')

# bbsContent = soup.select('div[class="bbs-content"]')
bbsContent = soup.select('div.bbs-content')
print('====')
print(bbsContent[0])
print('====')
print(bbsContent[0].findAll('div'))
print('====')
print(bbsContent[0].findAll('a'))