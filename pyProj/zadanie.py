m = (1, 2, 3, 4, 5, 6, 78, 8, 4, 5, 64, 3, 2, 34)
n = []
for i in range(len(m)):
    if (i + 1) % 2 != 0:
        n.append(i*m[i])
    else:
        n.append(m[i]/i)
n = tuple(n)
print(type(n))
print(n)
