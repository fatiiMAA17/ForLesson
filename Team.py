num = int(input())
s = 0
for i in range(0,num):
  a , b , c = map(int, input().split())
  if a + b + c >= 2:
    s += 1
print(s)