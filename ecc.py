# Eliptic Curve Cryptography

# P = (x1, y1) = (2, 9), Q = (x2, y2) = (3,10)
# D = P+Q = (x3,y3)
# m = (y2-y1) / (x2-x2)
# x3 = m^2 -x1-x2
# y3 = m(x1-x2)-y1

def eccSum(x1, x2, y1, y2):
    m = (y2-y1) / (x2-x1) if (x2-x1) != 0 else 0
    x3 = (m ** 2) - x1 - x2
    y3 = m * (x1-x2)-y1
    return x3, y3


x1 = 2
x2 = 3
y1 = 9
y2 = 10
x3, y3 = eccSum(x1, x2, y1, y2)
print("P + Q = (", x3, y3, ")")
# R = (x4, y4) = (-4, -3)
x4 = -4
y4 = -3

x, y = eccSum(x3, x4, y3, y4)  # (P + Q) + R
print("(P + Q) + R = (", x, y, ")")

a, b = eccSum(x2, x, y2, y)  # Q + R
c, d = eccSum(x1, a, y1, b)  # P + (Q+R)
print("Q+R = (", a, b, ")")
print("P + (Q+R) = (", c, d, ")")

# E : y2 = x3 + 73
# --> a = 0

a = 0


def productEcc(x, y, a):
    x3 = ((3*x**2 + a) / 2*y)**2 - 2*x
    y3 = -y + ((3*x**2 + a) / 2*y)*(x - x3)
    return x3, y3


xp, yp = productEcc(x1, y1, a)
print("2P = (", xp, ",", yp, ")")

p, r = eccSum(xp, x4, yp, y4)
print("2P + R = (", p, ",", r, ")")
