def fast_mul(a,b):
  result = 0
  while a:
    if ((a%2) & 1):
      result += b
    a = a >> 1
    b = b << 1
  return result
a = 5
b = 4

if (fast_mul(a,b)==a*b):
  print(fast_mul(a, b))

