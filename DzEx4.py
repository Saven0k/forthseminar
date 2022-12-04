from random import randint
from random import choice
import random
'''
4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.

*Пример:*

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''


a = 0
b = 0
c = 0
k = int(input("Enter cof k: "))


file = open('Ex4.txt', "w")
#(f'{a}x ** {k} + {b}x + {c} = 0'), (f'{a}x ** {k} + {c} = 0'), (f'{a}x ** {k} = 0')
lst = [1, 2, 3]
random_write = random.choice(lst)
if random_write == lst[1]:
    a = randint(1, 100)
    b = randint(1, 100)
    c = randint(1, 100)
    result1 = f'{a}x ** {k} + {b}x + {c} = 0'
elif random_write == lst[2]:
    a = randint(1, 100)
    c = randint(1, 100)
    result1 =  f'{a}x ** {k} + {b}x + {c} = 0'
else:
    a = randint(1, 100)
    result1 = f'{a}x ** {k} + {b}x + {c} = 0'
file.write(result1)

file.close()


#(f'{a1}x ** {k1} - {b1}x + {c1} = 0')

k1 = int(input("Enter cof k1: "))
#п
a1 = 0
b1 = 0
c1 = 0

file2 = open('Ex5.txt', "w")
#(f'{a1}x ** {k1} + {b1}x + {c1} = 0') , (f'{a1}x ** {k1} + {c1} = 0') , (f'{a1}x ** {k1} = 0')
lst2 = [1, 2, 3]
random_write2 = random.choice(lst2)

if random_write2 == lst2[1]:
    a1 = randint(1, 100)
    b1 = randint(1, 100)
    c1 = randint(1, 100)
    result = f'{a1}x ** {k1} + {b1}x + {c1} = 0'
elif random_write2 == lst2[2]:
    a1 = randint(1, 100)
    c1 = randint(1, 100)
    result = f'{a1}x ** {k1} + {c1} = 0'
else:
    a1 = randint(1, 100)
    result = f'{a1}x ** {k1} = 0'

file2.write(result)

file2.close()

