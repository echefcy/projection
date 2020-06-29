import math

def zero_matrix(rows, cols):
    mat = []
    for i in range(rows):
        r = []
        for j in range(cols):
            r.append(0)
        mat.append(r)
    return mat

def scale(a, m):
    ret = m
    for i in range(len(ret)):
        for j in range(len(ret[0])):
            ret[i][j] = a*ret[i][j]
    return ret

def add(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise SyntaxError("Matrix dimensions are not the same")
        return
    ret = []
    for i in range(0, len(m1)):
        r = []
        for j in range(0, len(m1[0])):
            r.append(m1[i][j] + m2[i][j])
        ret.append(r)
    return ret

def subtract(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise SyntaxError("Matrix dimensions are not the same")
        return
    ret = []
    for i in range(0, len(m1)):
        r = []
        for j in range(0, len(m1[0])):
            r.append(m1[i][j] - m2[i][j])
        ret.append(r)
    return ret

def multiply(m1, m2):
    if len(m1[0]) != len(m2):
        raise SyntaxError("Matrix dimensions unfit for multiplication")
    ret = []
    for i in range(0, len(m1)):
        r = []
        for j in range(0, len(m2[0])):
            sum = 0
            for k in range(0, len(m1[0])):
                sum += m1[i][k]*m2[k][j]
            r.append(sum)
        ret.append(r)
    return ret


# column vector operations

def magnitude(v):
    sum = 0
    for i in range(len(v)):
        sum += v[i][0]**2
    return math.sqrt(sum)

def normalize(v):
    m = magnitude(v)
    if m == 0:
        raise ZeroDivisionError
    return scale(1/m,v)

def dotprod(v1, v2):
    if len(v1) != len(v2):
        raise SyntaxError
    sum = 0
    for i in range(len(v1)):
        sum += v1[i][0]*v2[i][0]
    return sum

def crossprod(v1, v2):
    if len(v1) != 3 or len(v1) != len(v2):
        raise SyntaxError
    ret = [
        [v1[1][0]*v2[2][0]-v1[2][0]*v2[1][0]],
        [v1[2][0]*v2[0][0]-v1[0][0]*v2[2][0]],
        [v1[0][0]*v2[1][0]-v1[1][0]*v2[0][0]]
        ]
    return ret

if __name__ == "__main__":
    pass