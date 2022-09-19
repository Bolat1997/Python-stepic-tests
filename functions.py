# TEST1
# Напишите функцию draw_box(),
# которая выводит звездный прямоугольник
# с размерами 14×10 в соответствии с образцом:
# **********
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# **********

def draw_box():
    print("*" * 10)
    for i in range(12):
        i = "*        *"
        print(i)
    print("*" * 10)


draw_box()


# TEST2
# Напишите функцию draw_triangle(),
# которая выводит звездный прямоугольный
# треугольник с катетами, равными 10 в соответствии с образцом:

# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********

def draw_triangle():
    for i in range(1, 11):
        print("*" * i)


draw_triangle()


# TEST3
# Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
#
# fill – символ заполнитель;
# base – величина основания равнобедренного треугольника;
# а затем выводит его.
#
# Примечание: Гарантируется, что основание треугольника – нечетное число.

def draw_triangle(fill, base):
    t = (base + 1) // 2
    for i in range(1, t + 1):
        print(fill * i)
    for j in range(base - t, 0, -1):
        print(fill * j)


fill = input()
base = int(input())

draw_triangle("*", 9)


# TEST4
# Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
#
# name – имя человека;
# surname – фамилия человека;
# patronymic – отчество человека;
# а затем выводит на печать ФИО человека.
#
# Примечание. Предусмотрите тот факт, что все три буквы в ФИО должны иметь верхний регистр.

def print_fio(name, surname, patronymic):
    name_s = name[0].upper()
    surname_s = surname[0].upper()
    patronymic_s = patronymic[0].upper()
    print(surname_s, name_s, patronymic_s, sep="")


name = input()
surname = input()
patronymic = input()

print_fio(name, surname, patronymic)


# TEST5
# Напишите функцию convert_to_miles(km),
# которая принимает в качестве аргумента расстояние в километрах
# и возвращает расстояние в милях.
# Формула для преобразования: мили = километры * 0.6214.


def convert_to_miles(num):
    return num * 0.6214


num = int(input())
print(convert_to_miles(num))


# TEST6
# Напишите функцию get_next_prime(num),
# которая принимает в качестве аргумента натуральное число
# num и возвращает первое простое число большее числа num.
#
# Примечание 1. Используйте функцию is_prime() из предыдущей задачи.

def is_prime(num):
    count = 0
    if num == 1:
        return False
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False


def get_next_prime(num):
    while is_prime(num + 1) == False:
        num += 1
        continue
    return num + 1


num = int(input())
print(get_next_prime(num))


# TEST7
# Напишите функцию get_middle_point(x1, y1, x2, y2),
# которая принимает в качестве аргументов координаты концов отрезка (x1;y1),(x2;y2)
# и возвращает координаты точки являющейся серединой данного отрезка.

def get_middle_point(x1, y1, x2, y2):
    a = (x1 + x2) / 2
    b = (y1 + y2) / 2
    return a, b


x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
aget, bget = get_middle_point(x1, y1, x2, y2)
print(aget, bget)
