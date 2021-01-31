import requests
from bs4 import BeautifulSoup

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

landingPageUrl = 'https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html'
over18Url = 'https://www.ptt.cc'
pttUrl = 'https://www.ptt.cc/bbs/Gossiping/index.html'

ss = requests.session()

resLandingPage = ss.get(landingPageUrl, headers=headers)
soupLandingPage = BeautifulSoup(resLandingPage.text, 'html.parser')

data = dict()

# For hidden value
hiddenKey = soupLandingPage.select('input')[0]['name']
hiddenValue = soupLandingPage.select('input')[0]['value']
data[hiddenKey] = hiddenValue

# For button
buttonKey = soupLandingPage.select('button')[0]['name']
buttonValue = soupLandingPage.select('button')[0]['value']
data[buttonKey] = buttonValue

print(data)
print(ss.cookies)

# Get cookies
over18Url += soupLandingPage.select('form')[0]['action']
ss.post(over18Url, data=data)
print(ss.cookies)

res = ss.get(pttUrl, headers=headers)
print(res.text)
