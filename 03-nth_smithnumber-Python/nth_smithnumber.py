# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

def fun_nth_smithnumber(n):
    if n == 0:
        return 4

    count = 1
    i = 0
    while count <= n:
        i += 1
        if is_smith_number(i):
            count += 1
    return i


def is_smith_number(n):
    return digit_sum(n) == sum_prime_fact(n)


def digit_sum(n):
    res = 0
    while n > 0:
        rem = n % 10
        res += rem
        n //= 10
    return res


def sum_prime_fact(n):
    i = 2
    res = 0
    while n > 1:
        if n % i == 0:
            res += digit_sum(i)
            n //= i
        else:
            i += 1
    return res