num = input()
luckyNum = 0
for i in num:
  if i == '4' or i == '7':
    luckyNum += 1
if luckyNum == 4 or luckyNum == 7:
  print('YES')
else:
  print('NO')