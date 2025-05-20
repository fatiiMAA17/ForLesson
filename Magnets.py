n = int(input())
magnet = input().strip()
k = 1
for _ in range(n-1):
  s = input().strip()
  if s != magnet:
    k += 1
  magnet = s
print(k)
# n = int(input()); k =[]; c,s = 1,0
# for _ in range(n):
#   magnet = int(input())
#   k.append(magnet)
# for i in range(0,n-1):
#   if k[s] != k[s - 1]:
#     c += 1
# s += 1
# print(c)