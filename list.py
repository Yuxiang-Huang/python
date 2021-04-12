def make_list_one_to_n(n):
    g = []
    i = 1
    while i <= n:
        g.append(i)
        i+= 1
    return g
print(make_list_one_to_n(0))
print(make_list_one_to_n(1))
print(make_list_one_to_n(3))

def make_even_list_to_n(n):
    g = []
    i = 0
    while i <= n:
        g.append(i)
        i+= 2
    return g
print(make_even_list_to_n(0))
print(make_even_list_to_n(3))
print(make_even_list_to_n(6))

def make_sentence(g):
    s = ''
    i = 0
    while i < len(g):
        s+= g[i] + ' '
        i+= 1
    return s
print(make_sentence([]))
print(make_sentence(['bob']))
print(make_sentence(['hot', 'diggity', 'daffodil']))

def make_fib_list(n):
    if n == 0:
        return [0]
    g = [0, 1]
    i = 2
    while i <= n:
        new_fib = g[i-1] + g[i-2]
        g.append(new_fib)
        i+= 1
    return g
print(make_fib_list(0))
print(make_fib_list(1))
print(make_fib_list(2))
print(make_fib_list(6))

