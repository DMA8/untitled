P = [712,4,5,-122,4,6,4,1,20,0,0,2,3]
def quick(a:list):

    few = []
    eq = []
    gr = []
    if len(a) <=1:
        print('here')
        return a
    base = a[len(a)//2]
    for i in range(len(a)):
        if a[i] < base:
            few.append(a[i])
        elif a[i] > base:
            gr.append(a[i])
        else:
            eq.append(a[i])
    quick(few)
    quick(gr)

#Merge - слияние
#СОРТИРОКА СЛИЯНИЕМ

def merge(A:list, B:list):
    """
    нужно сделать слияние двух массивов в новый массив
    сравниваем поэлементно массивы, пихаем меньший из элементов в новый массив
    :param A:
    :param B:
    :return:
    """
    C = []
    A_counter = 0
    B_counter = 0
    while A_counter < len(A) and B_counter < len(B):
        if A[A_counter] <= B[B_counter]:
            C.append(A[A_counter])
            A_counter += 1
        else:
            C.append(B[B_counter])
            B_counter += 1
    while A_counter < len(A):
        C.append(A[A_counter])
        A_counter += 1
    while B_counter < len(B):
        C.append(B[B_counter])
        B_counter += 1
    return C


A = [2, 4, 6, 7]
B = [1, 2, 4, 5, 8, 9]
#print(merge(A, B))

def sort_sliyanie(to_sort):
    """
    1. Делим лист под сортировку на 2 части
    СОРТИРУЕМ 2 ЧАСТИ
    2. Сравниваем первые элемент левой части с первым элементом второй части, запихиваем меньший в отсортированный список, продолжаем сравнивать со след элементом

    :param to_sort:
    :return:
    """
    base = len(to_sort)//2
    if len(to_sort) <= 1:
        return
    L = to_sort[:base]
    R = to_sort[base:]
    sort_sliyanie(L)
    sort_sliyanie(R)
    out = merge(L,R)
    for i in range(len(to_sort)):
        to_sort[i] = out[i]
    return out



#print(sort_sliyanie(P))
def merge2(L,C,R):
    merged2 = []
    for i in L:
        merged2.append(i)
    for i in C:
        merged2.append(i)
    for i in R:
        merged2.append(i)
    return merged2


def quick(A:list):
    if len(A) <= 1:
        return
    barrier = A[0]
    L = [i for i in A if i < barrier]
    R = [i for i in A if i > barrier]
    C = [i for i in A if i == barrier]
    quick(L)
    quick(R)
    out = merge2(L,C,R)
    for i in range(len(out)):
        A[i] = out[i]
    return A


#print(quick(P))
#print(P)
i = 0
'''while i < len(P) - 1 and P[i] <= P[i+1]:
    i += 1
else:
    print('отсортирован')
P = [712,4,5,-122,4,6,4,1,20,0,0,2,3]
for i in range(len(P)-1):
    if P[i] <= P[i+1]:
        continue
    else:
        print('Неотсортирован', P[i], P[i+1])
        break
else:
    print('отсортирован')'''
'''def check_order(inp:list, order='True'):
    if order:
        for i in range(len(inp) - 1):
            if inp[i] <= inp[i + 1]:
                continue
            else:
                print('Неотсортирован', inp[i], inp[i + 1])
                return False

        else:
            print('отсортирован')
            return True
    else:
        for i in range(len(inp) - 1):
            if inp[i] >= inp[i + 1]:
                continue
            else:
                print('Неотсортирован', inp[i], inp[i + 1])
                return False
        else:
            return True
            print('отсортирован')'''

def check_order(inp:list, order=True):

    for i in range(len(inp) - 1):
        if order and inp[i] <= inp[i + 1] or not order and inp[i] >= inp[i+1]:
            continue
        else:
            print('Неотсортирован', inp[i], inp[i + 1])
            return False
    else:
        print('отсортирован')
        return True

#check_order(P, order=False)

tet = [12,21,34,45,51,60,77,89,102]

def search(inp:list, value:int):
    left = 0
    right = len(inp)-1
    mid = (left+right)//2
    if inp[mid] == value:
        return mid
    if value > inp[mid]:
        return search(inp[mid+1:],value) + (mid+1)
    else:
        return search(inp[:mid],value)
print(search(tet,45))





