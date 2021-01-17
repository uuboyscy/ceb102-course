tmpStr = 'test123ttttt'

# f = open('testWrite.txt', 'w', encoding='utf-8')
# f = open('testWrite.txt', 'a', encoding='utf-8')
with open('testWithWrite.txt', 'a', encoding='utf-8') as f:
    f.write(tmpStr)



