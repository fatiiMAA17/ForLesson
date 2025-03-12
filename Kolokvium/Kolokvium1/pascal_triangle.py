n = int(input())
a = 0
triangle = []
while n != 0:
    num = 11 ** a
    triangle.append(num)
    a += 1
    n = n - 1
    print(triangle)
    triangle.remove(num)