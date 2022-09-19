# TEST1
# Даны два целых числа m и n.
# Напишите программу, которая выводит все числа от m
# до n включительно в порядке возрастания, если m < n,
# или в порядке убывания в противном случае.

a = int(input())
b = int(input())
if a > b:
    for i in range(a, b - 1, -1):
        print(i)
elif b > a:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b + 1):
        print(i)

# TEST2
# Даны два целых числа m и n (m > n). Напишите программу,
# которая выводит все нечетные числа от m до n включительно в порядке убывания.

a = int(input())
b = int(input())
if a % 2 != 0:
    for i in range(a, b - 1, -2):
        print(i)
else:
    for i in range(a - 1, b - 1, -2):
        print(i)

# TEST3
# Даны два натуральных числа m и n ( m ≤ n).
# Напишите программу, которая выводит все числа
# от m до n включительно удовлетворяющие хотя бы одному из условий:
#
# число кратно 17;
# число оканчивается на 9;
# число кратно 3 и 5 одновременно.

a = int(input())
b = int(input())
for i in range(a, b + 1):
    if i % 17 == 0 or i % 10 == 9 or i % 3 == 0 and i % 5 == 0:
        print(i)

# TEST4
# Дано натуральное число n.
# Напишите программу, которая выводит таблицу умножения на n.

n = int(input())
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

# TEST5
# На вход программе подаются два целых числа a и b (a ≤ b).
# Напишите программу, которая подсчитывает количество чисел в диапазоне
# от a до b включительно, куб которых оканчивается на 4 или 9.

a = int(input())
b = int(input())
total = 0
for i in range(a, b + 1):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        total += 1
print(total)

# TEST6
# На вход программе подается натуральное число n.
# Напишите программу, которая вычисляет n!.

n = int(input())
num = 1
for i in range(1, n + 1):
    num *= i
print(num)

# TEST7
# На вход программе подается натуральное число n,
# а затем n различных натуральных чисел, каждое на отдельной строке.
# Напишите программу,которая выводит наибольшее
# и второе наибольшее число последовательности.

n = int(input())
largest = 0
prelargest = 0
for i in range(1, n + 1):
    b = int(input())
    if b > largest:
        prelargest = largest
        largest = b
    elif b < largest and b > prelargest:
        prelargest = b
print(largest)
print(prelargest)

# TEST8
# Напишите программу, которая считывает последовательность из 10 целых чисел
# и определяет является ли каждое из них четным или нет
# Программа должна вывести строку «YES», если все числа четные и «NO» в ином случае.

flag = 'YES'
for _ in range(10):
    a = int(input())
    if a % 2 != 0:
        flag = 'NO'
print(flag)

# TEST9
# Напишите программу, которая считывает натуральное число n
# и выводит первые n чисел последовательности Фибоначчи.

n = int(input())
total = 0
total_1 = 1
for i in range(n):
    total, total_1 = total_1, total + total_1
    print(total, end=" ")
