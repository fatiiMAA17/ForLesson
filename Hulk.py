n = int(input()); word = ''; a ='I hate it'; b ='I love it'; c ='I hate that'; d='I love that'
if n ==1:
  print(a)
  exit()
elif n == 2:
  print(c +' '+ b)
  exit()
while n > 2:
  word += ' '+ c +' '+ d
  n -= 2
print(word +' '+ a if n == 1 else word +' ' + c +' '+ b)