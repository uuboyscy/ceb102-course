import json

jsonData = {
    '001': {
        'Name': 'Allen',
        'Age': 22
    },
    '002': {
        'Name': 'Ted',
        'Age': 25
    }
}

jsonStr = json.dumps(jsonData)
print(jsonStr)
with open('test.json', 'w', encoding='utf-8') as f:
    f.write(jsonStr)


with open('test.json', 'r', encoding='utf-8') as f:
    jsonStr2 = f.read()

jsonData2 = json.loads(jsonStr2)
print(jsonData2)

print(type(jsonStr2))
print(type(jsonData2))