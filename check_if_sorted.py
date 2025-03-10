nums = input().split()
i = 0

def is_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

print(is_sorted(nums))