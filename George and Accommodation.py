n = int(input()); s = 0
for _ in range(n):
  n = list(map(int, input().split()))
  if n[1] != n[0] :
    if n[1] - n[0] < 2:
      s == 0
    else:
      s += 1
print(s)