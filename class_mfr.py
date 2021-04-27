

def remain4(a):
    return a % 4
def cap_start(s):
    return s[0] >= 'A' and s[0] <= 'Z'
def bigger(a, b):
    if a > b:
        return a
    else:
        return b


g = [4, 8, 13, 15, 16, 23, 42, 108]
print(g)
mod4 = list(map(remain4, g))
print("g % 4:", mod4)

s = 