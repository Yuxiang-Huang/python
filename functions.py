def distance(x0, y0, x1, y1):
    d = ((x1 - x0)**2 + (y1 - y0)**2)**0.5
    return d

print("distance(3, 0, 0, 4):", distance(3, 0, 0, 4))
print("distance(1, 0, 2, 0):", distance(1, 0, 2, 0))
print("distance(0, 0, 8, 15):", distance(0, 0, 8, 15))

def f_to_c(farenheit):
    celsius = (farenheit - 32) * 5/9
    return celsius

print("f_to_c(32.0):", f_to_c(32.0))
print("f_to_c(212.0):", f_to_c(212.0))
print("f_to_c(-40):", f_to_c(-40))

def eval_quadratic(a, b, c, x):
    y = a*x**2 + b*x + c
    return y

print("eval_quadratic(1, 0, 3, 1):", eval_quadratic(1, 0, 3, 1))
print("eval_quadratic(1, 2, 3, 1):", eval_quadratic(1, 2, 3, 1))
print("eval_quadratic(1, 0, 3, 2)", eval_quadratic(1, 0, 3, 2))

def is_even(n):
    return n % 2 == 0

print("is_even(12):", is_even(12))
print("is_even(11):", is_even(11))
print("is_even(0):", is_even(0))

def sleep_in(weekday, vacation):
    return vacation or not weekday

print("sleep_in(False, False):", sleep_in(False, False))
print("sleep_in(True, False):", sleep_in(True, False))
print("sleep_in(False, True):", sleep_in(False, True))

def near_hundred(n):
    hundo_distance = abs(100 - n)
    twohundo_distance = abs(200 - n)
    return( hundo_distance <= 10) or (twohundo_distance <= 10)
print("near_hundred(93):", near_hundred(93))
print("near_hundred(90):", near_hundred(90))
print("near_hundred(89):", near_hundred(89))
print("near_hundred(89):", near_hundred(110))
print("near_hundred(89):", near_hundred(204))