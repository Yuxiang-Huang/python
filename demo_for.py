g = [73, 9, 3, 42]
print(g)
print("for")
for e in g:
    e = e * -1
    print(e)
print(g)

print("while")
i = 0
while i < len(g):
    g[i] = g[i] * -1
    print(g[i])
    i+= 1
print(g)
