numOfcolor = int(input())
a = 0; color = list(input()); x = len(color)
if x == numOfcolor:
  for i in range(x):
    if x > i + 1:
      if color[i] == color[i+1]:
        a += 1
print(a)