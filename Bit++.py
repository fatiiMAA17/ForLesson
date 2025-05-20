num = int(input())
x = 0
if num >= 1 and num <= 150:
  for i in range(0,num):
    operation = input()
    if operation == "++":
      print(f'X {operation}')
    elif operation == "--":
      print(f'X {operation}')
    if "++" in operation:
      x += 1
    elif "--" in operation:
      x -=1
    else:
      print("This operation is not recognized!")
else:
  print('The number you enter do not pay for the condition!')
print(x)