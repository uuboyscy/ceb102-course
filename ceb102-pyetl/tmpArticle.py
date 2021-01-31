import requests
from bs4 import BeautifulSoup

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

urlTitle = 'https://www.ptt.cc/bbs/movie/M.1612016560.A.90E.html'

resArticle = requests.get(urlTitle, headers=headers)
soupArticle = BeautifulSoup(resArticle.text, 'html.parser')

articleContent = soupArticle.select('div[id="main-content"]')[0]
# print(articleContent.text.split('※ 發信站')[0])

# for i in articleContent.select('span'):
#     i.extract()
# for i in articleContent.select('div'):
#     i.extract()

for tag in ['span', 'div']:
    for i in articleContent.select(tag):
        i.extract()

print(articleContent.text)
