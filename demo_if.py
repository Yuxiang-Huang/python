def c_to_f(celsius):
   farenheit = (celsius * 9/5) + 32
   return farenheit

f = c_to_f(100)
print("c_to_f(100): ", f)

def f_to_c(farenheit):
    celsius = (farenheit - 32) * 5/9
    return celsius

c = f_to_c(212)
print("f_to_c(212): ", c)

# farenheit == True when temp is in f
def temp_convert(temp, farenheit):
    if farenheit:
        return f_to_c(temp)
    else:
        return c_to_f(temp)
    

# a: 90+
# b: 80 - 90
# c: 70 - 80
# d: 65 - 70
# f: < 65
def grade_convert(grade):
    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")
    elif grade >= 65:
        print("D")
    else:
        print("F")

