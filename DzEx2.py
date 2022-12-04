'''
2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

*Пример*

- при N=236     ->        [2, 2, 59]

'''
number = int(input("enter some number: "))
def simple_numbers(n):
    lst = []
    def fk(n):
        if n != 1 and n != 2:
            for i in range(2, n):
                if i % i == 0 and i % 1 == 0 and i % (i+1) != 0:
                    if n % i == 0:
                        lst.append(i)
                        if n == 1:
                            break
                        else:
                            n = n / i
                            fk(int(n))

                    else:
                        continue
                else:
                    continue
        elif n == 1:
            print(lst)
    fk(number)


simple_numbers(number)
