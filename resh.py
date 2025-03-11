import math


def welcome():
    print(
        "1 - Теорема Пифагора\n2 - Шины\n3 - Квадратное уравнение\n4 - Круг\n5 - Перевод СС\n6 - Прогрессия"
    )
    num = int(input("Введите номер нужной функции: "))
    if num == 1:
        pythagoras()
    elif num == 2:
        tires()
    elif num == 3:
        quadratic_equation()
    elif num == 4:
        circle()
    elif num == 5:
        notation()
    elif num == 6:
        progression()
    else:
        print("Не выбран ни один из возможных вариантов.")
        returning()


def returning():
    print(
        "1 - Теорема Пифагора\n2 - Шины\n3 - Квадратное уравнение\n4 - Круг\n5 - Перевод СС\n6 - Прогрессия"
    )
    num = int(input("Введите номер нужной функции: "))
    if num == 1:
        pythagoras()
    elif num == 2:
        tires()
    elif num == 3:
        quadratic_equation()
    elif num == 4:
        circle()
    elif num == 5:
        notation()
    elif num == 6:
        progression()
    else:
        print("Не выбран ни один из возможных вариантов.")
        returning()


def pythagoras_cath():
    a = float(input("Введите длину первого катета: "))
    b = float(input("Введите длину гипотенузы: "))
    c = b**2 - a**2
    print("Длина неизвестного катета: корень из", c)
    print("Длина неизвестного катета:", math.sqrt(c), "\n")
    returning()


def pythagoras_hypo():
    a = float(input("Введите длину первого катета: "))
    b = float(input("Введите длину второго катета: "))
    c = a**2 + b**2
    print("Длина гипотенузы: корень из", c)
    print("Длина гипотенузы:", math.sqrt(c), "\n")
    returning()


def pythagoras():
    print(
        "1 - Найти гипотенузу по двум катетам\n2 - Найти катет по гипотенузе и катету"
    )
    pyth_num = int(input("Введите номер нужной функции: "))
    if pyth_num == 1:
        pythagoras_hypo()
    elif pyth_num == 2:
        pythagoras_cath()


def tires():
    a = str(input("Введите маркировку шины: "))
    width = a[0:3]
    coef = a[4:6]
    coef = int(coef) / 100
    h = int(width) * coef
    h = round(h, 1)
    d1 = a[-2:]
    d = int(d1) * 25.4
    d = round(d, 1)
    D = 2 * h + d
    print("Высота боковины:", h)
    print("Диаметр диска:", d)
    print("Диаметр колеса:", D, "\n")
    returning()


def quadratic_equation():
    a = float(input("Введите коэффицент a: "))
    b = float(input("Введите коэффицент b: "))
    c = float(input("Введите число c: "))
    D = b**2 - (4 * a * c)
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print("Дискриминант:", D)
        print("Первый корень:", x1)
        print("Второй корень:", x2, "\n")
    elif D == 0:
        x1 = (-b) / (2 * a)
        print("Дискриминант:", D)
        print("Корень равен:", x1, "\n")
    else:
        x1 = (-b + (1j * math.sqrt(math.fabs(D)))) / (2 * a)
        x2 = (-b - (1j * math.sqrt(math.fabs(D)))) / (2 * a)
        print("Дискриминант:", D)
        print("Первый комплексный корень:", x1)
        print("Второй комплексный корень:", x2, "\n")
    returning()


def circle_lenght():
    pi = float(input("Введите число пи: "))
    r = float(input("Введите радиус: "))
    C = 2 * pi * r
    print("Длина окружности:", C, "\n")
    returning()


def circle_area():
    pi = float(input("Введите число пи: "))
    r = float(input("Введите радиус: "))
    S = pi * (r**2)
    print("Площадь круга:", S, "\n")
    returning()


def circle():
    print("1 - Длина окружности\n2 - Площадь круга")
    circle_num = int(input("Введите номер нужной функции: "))
    if circle_num == 1:
        circle_lenght()
    elif circle_num == 2:
        circle_area()


def notation():
    print("1 - 10 в 2\n2 - 10 в 8\n3 - 10 в 16\n4 - 2 в 10\n5 - 8 в 10\n6 - 16 в 10")
    notation_num = int(input("Введите номер нужного перевода: "))
    if notation_num == 1:
        print(bin(int(input("Введите число: ")))[2:], "\n")
    elif notation_num == 2:
        print(oct(int(input("Введите число: ")))[2:], "\n")
    elif notation_num == 3:
        print(hex(int(input("Введите число: ")))[2:], "\n")
    elif notation_num == 4:
        print(int(str(input("Введите двоичное число: ")), 2), "\n")
    elif notation_num == 5:
        print(int(str(input("Введите восьмеричное число: ")), 8), "\n")
    elif notation_num == 6:
        print(int(str(input("Введите шестнадцатеричное число: ")), 16), "\n")
    returning()


def arith_sum():
    a1 = int(input("Введите первый член арифметической прогрессии: "))
    an = int(input("Введите n-ый член арифметической прогрессии: "))
    n = int(input("Введите n: "))
    S = ((a1 + an) / 2) * n
    S = int(S)
    print("Сумма первых n членов арифметической прогрессии:", S, "\n")
    returning()


def arith_an():
    a1 = int(input("Введите первый член арифметической прогрессии: "))
    d = int(input("Введите разность арифметической прогрессии: "))
    n = int(input("Введите n: "))
    an = a1 + (d * (n - 1))
    print("n-ый член арифметической прогрессии равен:", an, "\n")
    returning()


def arithmetic():
    print("1 - Сумма первых n членов\n2 - n-ый член прогрессии")
    num = int(input("Введите номер нужной функции: "))
    if num == 1:
        arith_sum()
    elif num == 2:
        arith_an()


def geom_sum():
    b1 = float(input("Введите первый член геометрической прогрессии: "))
    bn = float(input("Введите n-ый член геометрической прогрессии: "))
    q = float(input("Введите знаменатель прогрессии: "))
    S = ((bn * q) - b1) / (q - 1)
    print("Сумма первых n членов геометрической прогрессии:", S, "\n")
    returning()


def geom_bn():
    b1 = float(input("Введите первый член геометрической прогрессии: "))
    q = float(input("Введите знаменатель прогрессии: "))
    n = int(input("Введите n: "))
    bn = b1 * (q ** (n - 1))
    print("n-ый член геометрической прогрессии равен:", bn, "\n")
    returning()


def geometric():
    print("1 - Сумма первых n членов\n2 - n-ый член прогрессии")
    num = int(input("Введите номер нужной функции: "))
    if num == 1:
        geom_sum()
    elif num == 2:
        geom_bn()


def progression():
    print("1 - Арифметическая прогрессия\n2 - Геометрическая прогрессия")
    num = int(input("Введите номер нужного раздела: "))
    if num == 1:
        arithmetic()
    elif num == 2:
        geometric()


welcome()
