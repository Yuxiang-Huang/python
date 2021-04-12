def split_name(s):
    space = s.find(' ')
    start = s[:space]
    end = s[space+1:]
    return start + '\n' + end

print( split_name('John Shaft'))


def bondify(name):
    s = ''
    space = name.find(' ')
    start = name[space+1:]
    return start + '... ' + name

print (bondify('Mr DW'))

def find_last(s, key):
    news = s[::-1]
    spot = news.find(key)
    if spot == -1:
        return spot
    return len(s) - 1 - spot

print(find_last( 'hello', 'l'))# ==> 3
print(find_last('hello', 'h'))# ==> 0
print(find_last('hello', 'z')) # ==> -1


def replace(s, key, r):
    rep_start = s.find(key)
    if rep_start == -1:
        return s
    else:
        start = s[:rep_start]
        end = s[(rep_start + len(key)):]
        return start + r + end
print(replace("I hate cs!", "hate", "love"))