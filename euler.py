def mult35sum(n):
    sum = 0
    i = 0
    while i < n:
        if (i % 3 == 0 or
            i % 5 == 0):
            sum+= i
        i+= 1
    return sum

print("problem 1(10):", mult35sum(10))
print("problem 1(1000):", mult35sum(1000))

def sum_of_squares(n):
    sum = 0
    i = 0
    while i <= n:
        sum+= i*i
        i+= 1
    return sum
def square_of_sum(n):
    sum = 0
    i = 0
    while i <= n:
        sum+= i
        i+= 1
    return sum * sum
def sum_diff(n):
    return square_of_sum(n) - sum_of_squares(n)

print("problem 6(10):", sum_diff(10))
print("problem 6(100):", sum_diff(100))


def lcm(max_divisor, guess):
    m = guess
    while m % max_divisor != 0:
        m+= guess
    return m
def combo_lcm(n):
    guess = n
    max_divisor = 1
    while max_divisor<= n:
        guess = lcm(max_divisor, guess)
        max_divisor+= 1
    return guess

print("problem 5(10):", combo_lcm(10))
print("problem 5(20):", combo_lcm(20))