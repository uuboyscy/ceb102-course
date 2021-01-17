tmpStr = 'test123ttttt'

# f = open('testWrite.txt', 'w', encoding='utf-8')
f = open('testWrite.txt', 'a', encoding='utf-8')

f.write(tmpStr)

f.close()

strList = ['test1', 'test2', 'test3']

# f = open('testWrite.txt', 'w', encoding='utf-8')
f = open('testWriteList.txt', 'a', encoding='utf-8')

for eachStr in strList:
    f.write(eachStr + '\n')

f.close()
