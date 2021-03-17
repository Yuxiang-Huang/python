def find_letter(s, c):
    i = 0
    while i < len(s):
        if s[i] == c:
            return i
        i+= 1
    #if we get to here, c does not appear in i
    return -1
        
print("find_letter('fish', 'f'):", find_letter('fish', 'f'))
print("find_letter('fish', 'F'):", find_letter('fish', 'F'))
print("find_letter('fish', 'h'):", find_letter('fish', 'h'))


def count_letter(s, c):
    i = 0
    count = 0
    while i < len(s):
        if s[i] == c:
            count+= 1
        i+= 1
    return count

print("count_letter('fishiii', 'i'):", count_letter('fishiii', 'i'))
print("count_letter('fishiii', 'f'):", count_letter('fishiii', 'f'))
print("count_letter('fishiii', 'I'):", count_letter('fishiii', 'I'))

def is_vowel(c):
    return (c == 'a' or c == 'A' or
            c == 'e' or c == 'E' or
            c == 'i' or c == 'I' or
            c == 'o' or c == 'O' or
            c == 'u' or c == 'U')
    
print("is_vowel('a'):", is_vowel('a'))
print("is_vowel('E'):", is_vowel('E'))
print("is_vowel('I'):", is_vowel('I'))
print("is_vowel('eieio'):", is_vowel('eieio'))


def count_vowels(s):
    i = 0
    count = 0
    while i < len(s):
        if is_vowel(s[i]):
            count+= 1
        i+= 1
    return count
        
print("count_vowels('fash'):", count_vowels('fash'))
print("count_vowels('fishi'):", count_vowels('fishi'))
print("count_vowels('faAsh'):", count_vowels('faAsh'))

def is_cap(c):
    if (len(c) == 1 and
        c >= 'A' and c <= 'Z'):
        return True
    else:
        return False
print("is_cap('x'):", is_cap('x'))
print("is_cap('F'):", is_cap('F'))
print("is_cap('Hello'):", is_cap('Hello'))