import glob

print(glob.glob('./test*'))
print(glob.glob('./*txt'))
print(glob.glob('./*.py'))
print(glob.glob('./test[2-4]*'))

print(glob.glob('./*txt')[0:3])
