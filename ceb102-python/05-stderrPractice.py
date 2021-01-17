import sys

tmpList = [1, 2, 3]
sys.stderr = open('./testError.txt', 'w')
print(tmpList[3])