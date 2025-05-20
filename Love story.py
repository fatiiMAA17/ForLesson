n = int(input()); k = 0
word = ["c", "o", "d", "e", "f", "o", "r", "c", "e", "s"]
for _ in range(n):
  new_word = list(input())
  k = 0
  for i in range(0,10):
    if new_word[i] != word[i]:
      k += 1
  print(k)