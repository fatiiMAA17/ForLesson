# enter_num = input().split()
# print(enter_num)
# unique_num = set(enter_num)
# print(sorted(unique_num))

num = input("enter numbers: ").split()
list = []
for a in num:
    if a not in list:
        list.append(a)
print(list)

