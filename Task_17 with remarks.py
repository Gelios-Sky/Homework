print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
discr = b ** 2 - 4 * a * c
print("Дискриминант=", discr)
def equation(a,b,):
    import math
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    return (x1,x2)
def equation_2(a,b,):
    x = -b / (2 * a)
    print("x=", x)
if discr > 0:
    print(equation(a,b,))
elif discr == 0:
    print(equation_2(a,b,))
else:
    print("Корней нет")





