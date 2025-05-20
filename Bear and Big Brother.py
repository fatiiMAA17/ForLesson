a , b = map(int, input().split())
s =  0
while a <= b:
  a *= 3; b *= 2; s += 1
if a > b:
  print(s)