def second_largest(arr):
    if len(arr) < 2:
        return None  # Not enough elements

    first, second = float('-inf'), float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second if second != float('-inf') else None

user_input = input("Siyahının elementlərini boşluqla ayıraraq daxil edin: ")
nums = list(map(int, user_input.split()))  # Daxil edilən ədədləri tam ədədə çeviririk

result = second_largest(nums)
print("İkinci ən böyük ədəd:", result)
