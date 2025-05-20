n = int(input()); s = 0
for _ in range(n):
  a,b = map(int, input().split())
  remainder = a % b
  if remainder == 0:
    print(0)
  else:
    print(b - remainder)
  # while a % b != 0:
  #   a += 1
  #   s += 1
  # if a % b == 0:
  #   print(s)