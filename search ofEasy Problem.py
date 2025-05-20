n = int(input()); s = 0
nums = list(map(int, input().split()))
for i in range(0,n):
  if nums[i] == 1:
    s += 1
if s >= 1 :
  print("HARD")
else:
  print("EASY")