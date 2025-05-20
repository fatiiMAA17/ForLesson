w = int(input())
i = 1
while i < w:
    s = w - i
    if s % 2 == 0 and i % 2 == 0:
        print("yes")
        break
    i = i + 1
    continue

else:
    print("no")

