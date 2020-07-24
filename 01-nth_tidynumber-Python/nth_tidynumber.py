# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def fun_nth_tidynumber(n):
    count = 0
    num = 1

    while count <= n:
        if isTidyNumber(num):
            count += 1
        num += 1
    return num

def isTidyNumber(n):
    temp = 10

    while n > 0:
        rem = n % 10
        n //= 10

        if rem > temp:
            return False
        temp = rem
    
    return True