import requests
import cloudscraper
import json
import pprint
import os
import ssl
from urllib import request
ssl._create_default_https_context=ssl._create_unverified_context

dcardFolder = 'dcard/'
if not os.path.exists(dcardFolder):
    os.mkdir(dcardFolder)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}

url = 'https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=30&before=235214594'
scraper = cloudscraper.create_scraper()

# res = requests.get(url, headers=headers)
jsonData = scraper.get(url).json()
# with open('jsondata.json', 'r', encoding='utf-8') as f:
#     jsonData = json.loads(f.read()) # list

# print(res.text)
# jsonData = json.loads(res.text) # list
# for i in jsonData:
#     print(i)
# pprint.pprint(jsonData[0])
# print(jsonData[0].keys())

for articleObj in jsonData:
    title = articleObj['title']
    articleUrl = 'https://www.dcard.tw/f/photography/p/' + str(articleObj['id'])
    print(title)
    print(articleUrl)
    for n, imgInfo in enumerate(articleObj['mediaMeta']):
        tmpImgUrl = imgInfo['url']
        imgPath = dcardFolder + title + "_" + str(n) + "." + tmpImgUrl.split('.')[-1]
        print('\t', tmpImgUrl)
        # request.urlretrieve(tmpImgUrl, dcardFolder + tmpImgUrl.split('/')[-1])
        # request.urlretrieve(tmpImgUrl, imgPath)
        resImg = requests.get(tmpImgUrl, headers=headers)
        imgContent = resImg.content
        with open(imgPath, 'wb') as f:
            f.write(imgContent)
    print('=====')