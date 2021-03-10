def sumAtoB(a, b):
    sum = 0
    while a <= b:
        sum+= a
        a+= 1
    return sum

print("sumAtoB(0, 1):", sumAtoB(0, 1))
print("sumAtoB(1, 3):", sumAtoB(1, 3))
print("sumAtoB(2, 0):", sumAtoB(2, 0))


def sum4s(n):
    sum = 0
    i = 1
    while i < n:
        if i % 4 == 0:
            sum+= i
        i+= 1
    return sum

print("sum4s(10):", sum4s(10))
print("sum4s(20):", sum4s(20))


def fizzbuzz(n):
    i = 1
    while i <= n:
        if i % 15 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
        i+= 1

fizzbuzz(20)

def sum_digs(n):
    sum = 0
    while n > 0:
        sum+= n % 10
        n = n // 10
    return sum

print("sum_digs(3):", sum_digs(3))
print("sum_digs(6732):", sum_digs(6732))


def num_digs(n):
    num = 0
    while n > 0:
        num+= 1
        n = n // 10
    return num

print("num_digs(3):", num_digs(3))
print("num_digs(6732):", num_digs(6732))

def num_digs_binary(n):
    num = 0
    while n > 0:
        num+= 1
        n = n // 2
    return num

print("num_digs_binary(2):", num_digs_binary(2))
print("num_digs_binary(10):", num_digs_binary(10))


# Look at num_digs and num_digs_binary, notice
# the only difference is the base you keep dividing by.
# We can make a more generic num_digs function that takes
# the base as an extra paramter.
def num_digs_better(n, base):
    num = 0
    while n > 0:
        num+= 1
        n = n // base
    return num