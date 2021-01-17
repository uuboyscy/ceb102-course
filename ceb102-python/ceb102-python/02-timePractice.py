import time

print(time.time())
for i in range(0, 5):
    print(i)
    # time.sleep(1)
print(time.localtime())
print(time.gmtime())
print(time.asctime())

timeNow = time.localtime()
timStr = time.strftime('Now datetime => %Y_%m_%d', timeNow)
print(timStr)