import random
from timeit import default_timer
start_time = default_timer()

def matrix(a, b, line1, column2, line2):
    if column2 == line1:
        result = []
        result_2 = []
        for i in range(line1):
            for j in range(column2):
                s = 0
                for k in range(line2):
                    s = s + a[i][k] * b[k][j]
                result_2.append(s)
            result.append(result_2)
            result_2 = []
        return result


# n1 = int(input('Введите количество строк в 1 матрице: '))
# m1 = int(input('Введите количество столбцов в 1 матрице: '))
# n2 = int(input('Введите количество строк во 2 матрице: '))
# m2 = int(input('Введите количество столбцов во 2 матрице: '))
n1 = int(10000)
n2 = int(10000)
m1 = int(10000)
m2 = int(10000)
matrix1 = [[random.randint(0, 10) for i in range(m1)] for j in range(n1)]
matrix2 = [[random.randint(0, 10) for k in range(m2)] for l in range(n2)]

# print('1 матрица: ')
# for elem in matrix1:
#     print(elem)
#
# print('2 матрица: ')
# for elem in matrix2:
#     print(elem)
# print('умножение этих матриц: ')
# for elem in matrix((matrix1),(matrix2), n1, m2, n2):
#     print(elem)
stop_time = default_timer()
matrix(matrix1,matrix2,n1,m2,n2)
print(stop_time-start_time)