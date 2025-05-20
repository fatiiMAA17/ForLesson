m,n = map(int, input().split())
k = 0
s = m * n
if 1 <= m and m <= n and n <= 16:
  if s % 2 == 0:
     while s != 0:
        s = s - 2
        k += 1
  elif s % 2 != 0:
    while s != 1:
        s = s - 2
        k += 1
  print(k)
else:
  print("The number you enter do not pay for the condition!")