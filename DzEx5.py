import random
from random import randint
import DzEx4 as d
'''
5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.
'''




file4 = open('Ex4.txt', "r")

file5 = open('Ex5.txt', "r")

print(file4.readline())
print(file5.readline())

file4.close()
file5.close()



file_result = open('result.txt', "w")

result = f'{d.a + d.a1}(x ** {d.k + d.k1}) +  {d.b + d.b1}x +  {d.c + d.c1} = 0'

file_result.write(result)

file_result.close()