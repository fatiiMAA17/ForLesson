n = int(input())
s = input()
anton = s.count('A')
danik = s.count('D')
if anton > danik:
    print("Anton")
elif danik > anton:
    print("Danik")
else:
    print("Friendship")
# n = int(input()); anton , danik = 0,0
# for _ in range(n):
#   success = input()
# for i in range(n):
#   if success == 'A':
#     anton += 1
#   elif success == 'D':
#     danik +=1
# if anton > danik:
#   print("Anton")
# elif danik > anton:
#   print("Danik")
# else:
#   print("Friendship")


# n = int(input()); s = 0; anton = 0; danik = 0
# for _ in range(n):
#   lucky = list(input())
# for i in range(n + 1):
#   if lucky[s] == 'A':
#     anton += 1
#   else:
#     danik += 1
#   s += 1
# if anton > danik:
#   print("Anton")
# elif danik > anton:
#   print("Danik")
# else:
#   print("Friendship")