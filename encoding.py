def upcase(c):
    if c >= 'a' and c <= 'z':
        diff = ord('a') - ord('A')
        newc = ord(c) - diff
        c = chr(newc)
    return c
print("upcase('q'):", upcase('q'))
print("upcase('C'):", upcase('C'))
print("upcase('3'):", upcase('3'))










def upstring(s):
    news = ''
    i = 0
    while i < len(s):
        news+= upcase(s[i])
        i+= 1
    return news
print("upstring('hello'):", upstring('hello'))
print("upstring('What’s up?'):", upstring('What’s up?'))