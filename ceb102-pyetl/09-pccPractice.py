import requests
from bs4 import BeautifulSoup

headersStr = """Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7
Cache-Control: max-age=0
Connection: keep-alive
Content-Length: 479
Content-Type: application/x-www-form-urlencoded
Cookie: cookiesession1=1EF25D71ZAGAWZE7M8PDANFTANCWB7BD; ccsession=202009122259236601000a23c45cde; _ga=GA1.1.1806446161.1611974352; JSESSIONID=0000CQ2eCBJPTJJT9KL0Wxwhk0H:148b36dur; NSC_xfc_qfstjtufodf=ffffffff09081f7445525d5f4f58455e445a4a423660; _ga_Y7WTCDJF3D=GS1.1.1612075215.4.0.1612075215.0
Host: web.pcc.gov.tw
Origin: https://web.pcc.gov.tw
Referer: https://web.pcc.gov.tw/tps/pss/tender.do?method=goSearch&searchMode=common&searchType=advance&searchTarget=ATM
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"""

headers = dict()
for row in headersStr.split('\n'):
    headers[row.split(': ')[0]] = row.split(': ')[1]

# print(headers)

dataStr = """
method: search
searchMethod: true
searchTarget: ATM
orgName: 
orgId: 
hid_1: 1
tenderName: 
tenderId: 
tenderStatus: 5,6,20,28
tenderWay: 
awardAnnounceStartDate: 110/01/29
awardAnnounceEndDate: 110/01/29
proctrgCate: 
tenderRange: 
minBudget: 
maxBudget: 
item: 
hid_2: 1
gottenVendorName: 
gottenVendorId: 
hid_3: 1
submitVendorName: 
submitVendorId: 
location: 
execLocationArea: 
priorityCate: 
isReConstruct: 
btnQuery: 查詢
"""

data = {row.split(': ')[0]: row.split(': ')[1] for row in dataStr.split('\n') if row != ''}
print(data)

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

url = 'https://web.pcc.gov.tw/tps/pss/tender.do?method=goSearch&searchMode=common&searchType=advance&searchTarget=ATM'
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
hiddenInput = soup.select('input[type="hidden"]')
print(hiddenInput)

hiddenData = dict()
for i in hiddenInput:
    try:
        hiddenData[i['name']] = i['value']
    except:
        pass

print(hiddenData)