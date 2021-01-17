import sys
sys.path.append('./testdir')
import test
import test2

print(sys.path)
for i in sys.path:
    print(i)

t = test.Test()
print(t.add(1, 4))