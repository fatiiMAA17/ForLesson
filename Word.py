word = input()
print(word.upper() if sum(1 for c in word if c.isupper()) > len(word) / 2 else word.lower())