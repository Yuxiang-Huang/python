def closer_number(a, b, target):
    a_dist = abs(a - target)
    b_dist = abs(b - target)
    if a_dist < b_dist:
        return a
    else:
        return b
    
print("closerNumber(7, 16, 10):", closer_number(7, 16, 10))
print("closerNumber(16, 7, 10):", closer_number(16, 7, 10))
print("closerNumber(-5, 8, 0):", closer_number(-5, 8, 0))

#distance helper function for closer_point
def distance(x0, y0, x1, y1):
    d = ((x1 - x0)**2 + (y1 - y0)**2)**0.5
    return d

def closer_point(x0, y0, x1, y1, xt, yt):
    d0 = distance(x0, y0, xt, yt)
    d1 = distance(x1, y1, xt, yt)
    if d0 < d1:
        return("0 is closer to 2")
    elif d1 < d0:
        return("1 is closer to 2")
    else:
        return("0 and 1 are equidistant to 2")

print("closer_point(4, 0, 10, 0, 0, 0):", closer_point(4, 0, 10, 0, 0, 0))
print("closer_point(9, 0, 0, -3, 0, 0):", closer_point(9, 0, 0, -3, 0, 0))

def military_time(time, ampm):
    if time != 12:
        if ampm == 0:
            return time
        else:
            return time + 12
    else:
        if ampm == 0:
            return 0
        else:
            return 12
        
print("military_time(3, 0):", military_time(3, 0))
print("military_time(3, 1):", military_time(3, 1))
print("military_time(12, 0):", military_time(12, 0))
print("military_time(12, 1):", military_time(12, 1))

def sale_price(cost, weeks_on_sale):
    if weeks_on_sale == 0:
        return cost
    elif weeks_on_sale == 1:
        return cost * 0.75
    elif weeks_on_sale == 2:
        return cost * 0.5
    else:
        return cost * 0.25
    
print("sale_price(200, 0):", sale_price(200, 0))
print("sale_price(200, 1):", sale_price(200, 1))
print("sale_price(200, 2):", sale_price(200, 2))
print("sale_price(200, 3):", sale_price(200, 3))

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year %100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

print("is_leap_year(2012):", is_leap_year(2012))
print("is_leap_year(1900):", is_leap_year(1900))
print("is_leap_year(2000):", is_leap_year(2000))
print("is_leap_year(1983):", is_leap_year(1983))
  