import math


def F1(x):
    return math.cos(x) + 0.05 * (x ** 3) + math.log2(x ** 2)


def F2(point):
    x1 = point[0]
    x2 = point[1]
    return (x1 ** 2) * math.cos(x2) + 0.05 * (x2 ** 3) + math.log2(x2 ** 2)


def derivation(x, fun):
    h = 0.0001
    return round((fun(x + h) - fun(x)) / h, 2)


def gradient(point, fun):
    x1 = point[0]
    x2 = point[1]
    h = 0.0001
    point_x1 = [x1 + h, x2]
    point_x2 = [x1, x2 + h]
    x1 = (fun(point_x1) - fun(point)) / h
    x2 = (fun(point_x2) - fun(point)) / h
    list = [round(x1, 2), round(x2, 2)]
    return list


# def gradient_optimization_one_dim(x, fun):
#     h = 0.001
#     for i in range(0, 50):
#         x = x - h * (fun(x + h) - fun(x)) / h
#     return round(x, 2)

def gradient_optimization_one_dim(fun):
    h = 0.001
    x = 10
    for i in range(0, 50):
        x = x - h * (fun(x + h) - fun(x)) / h
    return round(x, 2)


def gradient_optimization_multi_dim(fun):
    x1 = 4.0
    x2 = 10.0
    h = 0.001
    point = [x1, x2]
    point_x1 = [x1 + h, x2]
    point_x2 = [x1, x2 + h]
    for i in range(0, 50):
        x1 = x1 - h * (fun(point_x1) - fun(point)) / h
        x2 = x2 - h * (fun(point_x2) - fun(point)) / h

    list = [round(x1, 2), round(x2, 2)]
    return list


point1 = [10, 1]
point2 = [4, 10]
print(derivation(10, F1))
print(gradient(point1, F2))
print(gradient_optimization_one_dim(F1))
print(gradient_optimization_multi_dim(F2))
