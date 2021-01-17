import time

print('123123', end='')
print('testtest')

print('test1', 'test2', 'test3')
print('test1', 'test2', 'test3', sep='|')

print('test1', 'test2', file=open('./testprint.txt', 'w'))

f = open('./testFluxh.txt', 'a')
for i in range(0, 5):
    print(i, file=f, flush=True)
    time.sleep(2)
f.close()
