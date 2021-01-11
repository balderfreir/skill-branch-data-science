import math


def F1(x):
    return math.cos(x) + 0.05 * (x ** 3) + math.log2(x ** 2)


def F2(x1, x2):
    return (x1 ** 2) * math.cos(x2) + 0.05 * (x2 ** 3) + math.log2(x2 ** 2)


def derivation(x, fun):
    h = 0.01
    return round((fun(x + h) - fun(x)) / (h), 2)


def gradient(point, fun):
    x1 = point[0]
    x2 = point[1]
    h = 0.01
    list = [round((fun(x1 + h, x2) - fun(x1 - h, x2)) / (2 * h), 2), round(((fun(x1, x2 + h) - fun(x1, x2)) / h), 2)]
    return list


def gradient_optimization_one_dim(x, fun):
    h = 0.001
    for i in range(0, 50):
        x = x - h * ((fun(x + h) - fun(x)) / (h))

    return round(x, 2)


def gradient_optimization_multi_dim(point, fun):
    x1 = point[0]
    x2 = point[1]
    h = 0.001
    for i in range(0, 50):
        x1 = x1 - h * ((fun(x1 + h, x2) - fun(x1, x2)) / h)
        x2 = x2 - h * ((fun(x1, x2 + h) - fun(x1, x2)) / h)
    list = [round(x1, 2), round(x2, 2)]
    return list

# print(derivation(10, F1))
# point1 = [10, 1]
#
# print(gradient(point1, F2))
#
# print(gradient_optimization_one_dim(10, F1))
#
# point2 = [4, 10]
# print(gradient_optimization_multi_dim(point2, F2))
