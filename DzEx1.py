'''
1 Вычислить число π c заданной точностью d

*Пример:*

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


#Формула выслениә пи((2**0.5) + (3 ** 0.5))

def find_pi():
    d = list(input("Enter the value of the number d: "))
    d2 = ''
    d3 = []
    for i in range(len(d)):
        d3.append(d[i].replace('.', '0'))
    pi = round(((2**0.5) + (3 ** 0.5)), (len(d) - 2))
    print(f' при $d =  {d2.join(d)}  π =  {pi}')
'''
def pi():
    count = 0
    d = float(input("Enter the value of the number d: "))
    while d < 1:
        d = d * 10
        count += 1
    k = 1
    x = 0
    for k in range(1, 1000000):
        x = x + 4 * ((-1) ** (k + 1)) / (2 * k - 1)
    print(round(x, count))
pi()

#Честно скажу задание вообще не понял делал по примеру)