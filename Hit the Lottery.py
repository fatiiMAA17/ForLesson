n = int(input())
nums = [100, 20, 10, 5, 1]
num = 0

for i in nums:
    num += n // i
    n %= i

print(num)