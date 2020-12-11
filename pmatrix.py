import random
from timeit import default_timer
start_time = default_timer()
def summa():
    # Вводим размер матриц
    # r1 = int(input('Элементов в строке в матрицы1: '))
    r1 = int(1000)
    # c1 = int(input('Элементов в солбце в матрицы1: '))
    c1 = int(1000)
    # r2 = int(input('Элементов в строке в матрицы2: '))
    r2 = int(1000)
    # c2 = int(input('Элементов в солбце в матрицы2: '))
    c2 = int(1000)
    A = []
    for i in range(r1):
        A.append([])
        for j in range(c1):
            A[i].append(random.randint(0,10))
    # print('A = ')
    # for q in A:
    #     print(q)
    # print('')
    B = []
    for q in range(r2):
        B.append([])
        for w in range(c2):
            B[q].append(random.randint(0,10))
    # #print('B = ')
    # for q in B:
    #     print(q)
    # print('')

    # Умножение
    s = 0  # сумма
    t = []  # временная матрица
    C = []  # конечная матрица
    if len(B) != len(A[0]):
        print("Матрицы не могут быть перемножены")
    else:
        r1 = len(A)  # количество строк в первой матрице
        c1 = len(A[0])  # Количество столбцов в 1
        r2 = c1  # и строк во 2ой матрице
        c2 = len(B[0])  # количество столбцов во 2ой матрице
        for z in range(0, r1):
            for j in range(0, c2):
                for i in range(0, c1):
                    s = s + A[z][i] * B[i][j]
                t.append(s)
                s = 0
            C.append(t)
            t = []
    return C
summa()
print(default_timer()-start_time)