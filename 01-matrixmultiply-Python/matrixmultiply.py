# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    r1 = len(m1)
    r2 = len(m2)
    c1 = len(m1[0])
    c2 = len(m2[0])
    
    if c1 == r1:
        res = []
        while len(r) < r1:
            res.append([])
            while len(res[-1] < c2):
                res[-1].append(0)
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m1)[0]):
                    res[i][j] += m1[i][k] * m2[k][j]
        return res
    return None
