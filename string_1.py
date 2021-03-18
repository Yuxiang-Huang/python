def closer_number_helper(a, b, target):
    a_dist = abs(a - target)
    b_dist = abs(b - target)
    if a_dist < b_dist:
        return a
    else:
        return b
    
def closer_number(a, b, target):
    closer = closer_number_helper(a, b, target)
    s = str(closer)
    s+= ' is closer to '
    s+= str(target)
    return s

print("closer_number(7, 16, 10):", closer_number(7, 16, 10))
print("closer_number (20, 3, 8):", closer_number (20, 3, 8))
print("closer_number (-5, 8, 0):", closer_number (-5, 8, 0))


# All of  the whitespace (newlines, tabs) in the
# HTML are not necessary, but very helpful for
# debugging.
def make_table(a, b):
    s = '''<table>
            <thead>
                <tr>
                    <th>n</th>
                    <th>n^2</th>
                    <th>sqrt n</th>
                </tr>
            </thead>
            <tbody>\n'''
    while a <= b:
        s+= '<tr>\n'
        s+= '<td>' + str(a) + '</td>\n'
        s+= '<td>' + str(a*a) + '</td>\n'
        s+= '<td>' + str(a**0.5) + '</td>\n'
        s+= '</tr>\n'
        a+= 1
    s+= '</tbody></table>'
    return s
print("make_table(1, 4):\n", make_table(1, 4))
