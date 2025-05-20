costOffirstbanana, soldierMoney, numofBanana = map(int,input().split())
s = 0
while numofBanana != 0:
  s += costOffirstbanana * numofBanana
  numofBanana -= 1
result = s - soldierMoney
if result <= 0:
  print("0")
else:
  print(result)