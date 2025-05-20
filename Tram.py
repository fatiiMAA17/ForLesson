# n = int(input()); s = 0; c = []
# for _ in range(n):
#   a , b = map(int, input().split())
# for i in range(n-1):
#   s += b - a
#   c.append(s)
# print(c[-1], "0")
# k = 6
# if c[-1] > 6:
#   print("The tram has a capacity of more than 6 people.")
# elif c[-1] <= 6:
#   print(k)

n = int(input());
capacity, k = 0, 0
for _ in range(n):
    a, b = map(int, input().split())
    k += b - a
    capacity = max(capacity, k)
print(capacity)