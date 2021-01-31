import requests
from bs4 import BeautifulSoup

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

url = 'https://www.ptt.cc/bbs/movie/index.html'

for i in range(0, 5):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    titles = soup.select('div.title')
    # print(titles)
    for titleSoup in titles:
        # title = titleSoup.select('a')[0].text
        title = titleSoup.select_one('a').text
        urlTitle = 'https://www.ptt.cc' + titleSoup.select_one('a')['href']
        print(title)
        print(urlTitle)
        print('======')

    lastPageButton = soup.select('a[class="btn wide"]')
    # print(lastPageButton)
    lastPageUrl = 'https://www.ptt.cc' + lastPageButton[1]['href']
    # print(lastPageUrl)
    url = lastPageUrl
