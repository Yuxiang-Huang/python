def count(n, c):
    freq = 0
    for e in c:
        if e == n:
            freq+= 1
    return freq
print(count(4, [1, 2, 3, 4]))
print(count('a', 'abracadabra'))

def doublify(g):
    newg = []
    for e in g:
        newg.append(e * 2)
    return newg
print(doublify([6, 3, -8, 3.5]))

def add_ten(g):
    i = 0
    while i < len(g):
        g[i]+= 10
        i+= 1
g = [1, 2, 3, 4]
add_ten(g)
print(g)
# Should print [11, 12, 13, 14]

def zip_lists(a, b):
    apos = 0
    bpos = 0
    g = []
    while apos < len(a) and bpos < len(b):
        g.append(a[apos])
        g.append(b[bpos])
        apos+= 1
        bpos+= 1
    g+= a[apos:]
    g+= b[bpos:]
    return g

print(zip_lists( [1,2,3] , ['a','b'] ))# ==> [1,'a',2,'b',3]
print(zip_lists( [1,2] , [5,5,5,5] ))#   ==> [1,5,2,5,5,5]
print(zip_lists( [1] , [] ))#            ==> [1]
