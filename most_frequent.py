k = int(input(""))
b = []
while k!=0:
	x = input("")
	b.append(x)
	k -= 1
h = len(b)
for i in range(h):
	s = 0
	h = b[i]
	e = b.count(k)
	if s<=e:
		s = e
		d = h
	else:
		continue
print(d)
