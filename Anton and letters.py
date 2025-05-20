lst = input()
word = re.findall(r'[a-z]', lst)
print(len(set(word)))

# k = list(set(input()))
# n = 0; i = 0
# for _ in range(0,len(k)):
#   if k[i] != k[i + 1]:
#     n += 1
#     i += 1
# print(n)