def print_matrix(A):
    """
    Допоміжна функція до алгоритму: вивидить матрицю 3х3
    """
    for i in range(3):
        for k in range(3):
            print(round(A[i][k], 3), end=' ')
        print('')


def print_vector(b):
    """
    Допоміжна функція до алгоритму: вивидить вектор стовпчик
    """
    for i in range(3):
        print(b[i])


def multi_matrix(A, B):
    """
    Функція повертає дабуток двох матриць розміром  3х3
    """
    C = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                C[i][j] += A[i][k]*B[k][j]
    return C


def multi_matrix_vector(A, b):
    """
    Функція повертає дабуток матриці розміром  3х3 та вектора з 3ма елементами
    """
    C = [0, 0, 0]
    for i in range(3):
        for k in range(3):
            C[i] += A[i][k]*b[k]
    return C


def gauss(A, b):
    d = 1 # визначник
    for i in range(len(b)):
        # матриця перестановки
        P = [[1, 0, 0],
             [0, 1, 0],
             [0, 0, 1]]
        #матриця переходу
        M = [[1, 0, 0],
             [0, 1, 0],
             [0, 0, 1]]
        # пошук максимального елемента по стопцях
        max_elem = abs(A[0][i])
        max_elem_d = A[i][i]
        max_pos = 0
        if i == 2:
            max_elem = abs(A[i][i])
            max_pos = i
        else:
            for k in range(1, len(b)):
                if abs(A[k][i]) > max_elem:
                    max_elem = abs(A[k][i])
                    max_elem_d = A[k][i]
                    max_pos = k
        d *= max_elem_d
        if i != 2:
            P[max_pos][max_pos] = 0
            P[i][max_pos] = 1
            P[i][i] = 0
            P[max_pos][i] = 1
        if P != [[1, 0, 0], [0, 1, 0], [0, 0, 1]]:
            d *= -1
        print("--------{} КРОК--------".format(i+1))
        print("Матриця P має вигляд:")
        print_matrix(P)
        A = multi_matrix(P, A)
        b = multi_matrix_vector(P, b)
        print("Матриця P*A має вигляд:")
        print_matrix(A)
        print("Вектор b має вигляд:")
        print_vector(b)
        for j in range(3):
            if j == i:
                M[j][j] = 1/A[i][i]
            if j > i:
                M[j][i] = -A[j][i]/A[i][i]
        print("Матриця M має вигляд:")
        print_matrix(M)
        print("Матриця M*P*A має вигляд:")
        A = multi_matrix(M, A)
        print_matrix(A)
        print("Вектор b має вигляд:")
        b = multi_matrix_vector(M, b)
        print_vector(b)
    print("----------------------")
    # зворотній хід
    X = [0, 0, 0]
    for i in range(2, -1, -1):
        X[i] = b[i] - sum(x*a for x, a in zip(X[i+1:], A[i][(i+1):]))
    print("Рішення:")
    print("\n".join("x{0} =\t{1:10.2f}".format(i+1, x) for i, x in enumerate(X)))
    print("Визначник: {}".format(d))
    return (X)


def inverse_gauss(A):
    """
    Обернена матриця до А методом Гаусса
    """
    E = [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]]
    X = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    for i in range(3):
        x = gauss(A, E[i])
        for j in range(3):
            X[j][i] = x[j]
    print("Обернена матриця методом Гаусса")
    print_matrix(X)
    return X


def norma(A):
    """
    Норма матриці: максимальне значення з сум абсолютних значень коеф. по строках
    """
    so = []
    for i in range(3):
        s = 0
        for j in range(3):
            s += abs(A[i][j])
        so.append(s)
    return max(so)


def cond(A):
    """
    Число обумовленості з нормою прямою і оберненої матриці
    """
    n = norma(A)
    m = norma(inverse_gauss(A))
    print("Число обумовленості:")
    print("||A|| = {}, ||A^-1|| = {}, cond(A) = {}".format(round(n, 3), round(m, 3), round(n*m, 3)))


# A = [
#     [1, 2, -1],
#     [2, -3, 2],
#     [3, 1, 1]
# ]
#
# b = [
#     2,
#     2,
#     8
# ]


A = [
    [2, -6, 1],
    [8, 1, -4],
    [-1, 1, 4]
]

b = [
    -9,
    6,
    5
]

gauss(A, b)
inverse_gauss(A)
cond(A)