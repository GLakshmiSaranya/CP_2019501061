# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.

import math

def fun_nth_kaprekarnumber(n):
    count = 0
    k_num = 1
    i = 1

    while count < n:
        if is_kaprekarnumber(i):
            count += 1
            k_num = i
        i += 1
    return k_num

def is_kaprekarnumber(n):
    sqr = str(n ** 2)
    l = len(sqr)

    for i in range(1, l):
        s1 = int("".join(sqr[ : i]))
        s2 = int("".join(sqr[i : ]))

        if s1 + s2 == n:
            return True
    return False
