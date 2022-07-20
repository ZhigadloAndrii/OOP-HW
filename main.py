def jacobi(A, b, e):
    dos = True
    for i in range(3):
        s = 0
        for j in range(3):
            if i != j:
                s += abs(A[i][j])
        if abs(A[i][i]) < s:
            dos = False
    if (dos == True):
        print("Достатня умова збіжності виконується")
    else:
        print("Достатня умова збіжності не виконується")
        return False
    x = []
    for i in range(len(b)):
        x.append([0])
    count = 0
    B = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    while True:
        nx = []
        for i in range(3):
            nxi = b[i]
            for j in range(3):
                if j != i:
                    nxi = nxi + (-A[i][j])*x[j][0]
                    B[i][j] = (-A[i][j])/A[i][i]
            nxi = nxi/A[i][i]
            nx.append([nxi])
        lc = []
        for i in range(len(x)):
            lc.append(abs(x[i][0]-nx[i][0]))
        for i in nx:
            print(round(i[0], 5), end=" ")
        print('')
        normB = []
        for i in range(3):
            nb = 0
            for j in range(3):
                nb += abs(B[i][j])
            normB.append(abs(nb))
        normB = max(normB)
        e1 = (1 - normB)/normB*e
        if count == 0 or max(lc) < e1:
            print("Норма векторів: {}".format(max(nx)[0]))
        if max(lc) < e1:
            print("Розв'язок: ")
            for i in nx:
                print(i[0])
            return nx
        x = nx
        count += 1


A = [
    [8, 1, -4],
    [2, -6, 1],
    [-1, 1, 4]
]

b = [
    6,
    -9,
    5
]

e = 0.0001

jacobi(A, b, e)

