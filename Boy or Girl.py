nameOfuser=list(input())
name=[]
for i in nameOfuser:
  if i not in name:
    name.append(i)
s = len(name)
print("IGNORE HIM!" if s % 2 == 1 else "CHAT WITH HER!")