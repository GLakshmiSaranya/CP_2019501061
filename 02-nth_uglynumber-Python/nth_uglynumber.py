# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number. 
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.

def fun_nth_uglynumber(n):
    count = 0
    num = 1

    while count < n:
        num += 1
        if isUglyNumber(num):
            count += 1
    return num

def isUglyNumber(n):
    if n == 0:
        return False
    
    for i in [2, 3, 5]:
        while n % i == 0:
            n //= i
    if n == 1:
        return True
    return False