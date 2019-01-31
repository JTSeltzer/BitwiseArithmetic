import sys

def convertToBin32(a):
  return map(int, list(format(int(a), '032b')))

def bitFlip(a):
  return [i^1 for i in a]

def bitwiseAdd(a, b, cin):
  finalSum = []
  lsbSum = ((a[-1] ^ b[-1]) ^ cin)
  cout = ((a[-1] & b[-1]) | ((a[-1] ^ b[-1]) & cin))
  
  a.pop(-1)
  b.pop(-1)
  
  if len(a) > 0:
    finalSum = bitwiseAdd(a, b, cout)
  
  finalSum.append(lsbSum)
  return finalSum


print int(''.join(map(str, bitwiseAdd(convertToBin32(9999), convertToBin32(150248), 0))), 2)

'''
sys.argv.pop(0)
for i in range(len(sys.argv)):
  print convertToBin32(sys.argv[i])
'''