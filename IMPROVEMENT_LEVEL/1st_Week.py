'''a = int(input())
b = int(input())
c = int(input())
'''
'''if a < b: a, b = b, a
if a < c: a, c = c, a
if b > c: b,c = c, b

print(a,b,c, sep='\n')


for i in range(10):
    print(i if not i%2 else 'not_even')'''
#list comprehenshion
'''a = [1,2,3,4,67,42,23,11,22,32,52]
b = [x**2 for x in a if not x % 2]
b = ['hui' if x % 2 else x**2 for x in a]'''
#КВАДРАТИЧНЫЕ КОДИРОВКИ
"""
сортировка вставками
1)сравниванием нулевой элемент с ближайшим справа. если сосед меньше, то меняем местами

"""
a = [1221221,  2489, 85, 52, 12, 634, 23, 22]
for i in range(len(a)-1):
    for k in range(i, -1, -1):
        if a[k] > a[k+1]:
            a[k+1], a[k] = a[k], a[k+1]
        else: break
print(a)

"""сортировка методом выбора
сразу ставим на первую позицию минимального
последующий поиск минимума проводим не затрагивая установленные позиции
"""


a = [9,2]

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] > a[j] : a[i],a[j] = a[j],a[i]
#print(a)

"""
bublesort 
ПОЧТИ КАК ВСТАВКИ, ТОЛЬКО СРАВНИВАЮТСЯ ТОЛЬКО 2 ЭЛЕМЕНТА И ВСЕ НАЧИНАЕТСЯ СНАЧАЛА
если попался самое большое число, то оно встанет на свое место
"""
a = [2,82,12,1,0,23,-99,2,789]

for i in range(len(a)):
    for j in range(len(a)-1-i):
        if a[j] > a[j+1] : a[j], a[j+1] = a[j+1], a[j]
#print(a)

"""СОРТИРОВКА ПОДСЧЕТОМ !!!!! O(n)
эффективен только с малым числом уникальных элементов

"""
# СЧИТАЕМ КОЛИЧЕСТВО КАЖДОГО УНИКАЛЬНОГО ЧИСЛА
"""
0:1
1:12
2:12
3:2
...
"""
a = [1,2,1,1,0,2,3,1,5,3,3,6,3,2,3,4,6,7,8,9,6,4,5,3,4,2,3,5,4,2,3,4,2,3,4,3,1,2,3,4,5,6,7,8,9]
base = [0]*10
for k in a:
    base[k]+=1
a_sorted = []
print(base)
for i in range(len(base)):
    for p in range(base[i]):
        a_sorted.append(i)
#print(a_sorted)
# 3! = 1*2*3
def factorial(n:int):
    assert n >= 0, 'факториал отриц. не определен'
    if n == 0:
        return 1
    return factorial(n-1)*n

#print(factorial(2))

#АЛГОРИТМ ЕВКЛИДА  (НАИБОЛЬШИЙ ОБЩИЙ ДЕЛИТЕЛЬ)

def nod(a,b):
    if a == 0 or b == 0:
        return a + b
    if a > b:
        a %= b
    else:
        b %= a
    return nod(a,b)

print(nod(12,24))

def gcd(a,b):
    if a == b:
        return a
    elif a>b:
        return gcd(a-b,b)
    else: #a<b
        return gcd(a,b-a)
print(gcd(12,24))


#БЫСТРЫЕ ВОЗВЕДЕНИЯ В СТЕПЕНЬ
"""
если степень 0, то ретурн 1
если степень нечетная, то уменьшаем степень на 1 и домножаем на число
если степень четная, то возводим число в квадрат и делим степень на 2
"""
def power(a,n):
    if n == 0 :return 1
    elif n %2: return power(a,n-1)*n
    else: return power(a**2,n//2)

print(pow(2,8568))






