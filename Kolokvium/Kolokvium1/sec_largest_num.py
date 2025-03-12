# numbers=input("Enter the numbers:").split()
# numbers=list(numbers)
# numbers.sort()
# print(numbers[-2])

numbers = input('Enter numbers: ').split()
for i in range(len(numbers)):
  for j in range(i+1, len(numbers)):
    if numbers[i]<numbers[j]:
      temp = numbers[i]
      numbers[i] = numbers[j]
      numbers[j] = temp
print(numbers[1])