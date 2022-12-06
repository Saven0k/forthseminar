'''
2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

*Пример*

- при N=236     ->        [2, 2, 59]
'''

number = int(input("enter some number: "))
def Factor(n):
    lst = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            lst.append(d)
            n = n // d
        else:
            d += 1
    if n > 1:
        lst.append(n)
    print(lst)
Factor(number)
