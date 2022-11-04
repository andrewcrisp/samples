import math
pie = 0.123456789
total = 0
prime_count = 0
div_by_zero_flag = False

def gcd(a, b):
    if b > a:
        c = b
        b = a
        a = c
    if b == 0:
        return 0
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)
print(pie)

for i in range(100000):
    total += 1
    a = math.floor(pie*10**4)
    b = math.floor(((pie * 10 ** 4) - math.floor((pie * 10 ** 4))) * 10 ** 4)
    if (gcd(a, b) == 1):
        prime_count += 1
    if div_by_zero_flag:
        prime_count -= 1
        div_by_zero_flag = False
    if prime_count == 0:
        prime_count = 1
        div_by_zero_flag = True
    pie = math.sqrt((6.0 * total) / prime_count)
print(pie)

