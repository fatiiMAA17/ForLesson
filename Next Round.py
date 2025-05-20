n, k = map(int, input().split())
nums = list(map(int, input().split()))
score = nums[k-1]
count = sum(1 for num in nums if num >= score and num > 0)
print(count)