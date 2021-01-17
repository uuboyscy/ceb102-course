f = open('./testFluxh.txt', 'r', encoding='utf-8')

# print(f.read())

# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

# line = f.readline()
# while line != '':
#     print(line)
#     line = f.readline()

print(f.readlines())

f.close()