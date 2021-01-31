from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
headers = {
    'User-Agent': userAgent
}
url = 'https://www.ptt.cc/bbs/joke/index.html'
# Initiate a request-object
req = request.Request(url=url, headers=headers)
res = request.urlopen(req)
html = res.read().decode('utf-8')
print(html)