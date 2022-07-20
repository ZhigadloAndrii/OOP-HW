import math


def f(x): return x ** 3 - 4.0 * x ** 2 - 4.0 * x + 13.0
def d_f(x): return 3.0*x**2 - 8.0*x - 4.0
def phi(x): return 4.0 + 4.0/x - 13.0/(x**2)
def d_phi(x): return (26.0 - 4.0*x)/(x**3)


# метод дихотримії
def bisection(a, b, e):
    if f(a) * f(b) >= 0:
        print("Невірний проміжок")
        return False

    i = 0
    print("BISECTION")
    n = math.trunc(math.log2((b - a) / e)) + 1
    print("апріорна оцінка {0}".format(n))

    while True:
        x = (a + b) / 2.0

        print(f"{i:3}|{round(x, 5):10}|{round(f(x), 5):10}")

        if abs(a - b) < 2 * e:
            break

        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
        i += 1


# метод простої ітерації
def simle_iteration(a, b, e):
    print("SIMPLE ITERATION")

    q = max(abs(d_phi(a)), abs(d_phi(b)))
    if q >= 1:
        print("Невірний проміжок")
        return False

    x0 = (a + b) / 2.0
    x1 = phi(x0)
    d = max(abs(a - x0), abs(b - x0))
    if abs(x1 - x0) > (1 - q)*d:
        print("Не виконується умова збіжності")
        return False

    i = 1

    n = math.trunc((math.log(abs(x1 - x0) / (1 - q) / e)) / math.log(1 / q)) + 1
    print("апріорна оцінка {0}".format(n))

    print(f"{0:3}|{round(x0, 5):10}|{round(f(x0), 5):10}")
    print(f"{i:3}|{round(x1, 5):10}|{round(f(x1), 5):10}")
    while abs((phi(x1) - x1)/(1 - (phi(x1)-x1)/(x1-x0))) >= e:
        i += 1
        x0 = x1
        x1 = phi(x1)
        print(f"{i:3}|{round(x1, 5):10}|{round(x0 - x1, 5):10}")
    print(f"{i+1:3}|{round(phi(x1), 5):10}|{round(x1 - phi(x1), 5):10}")


# метод релаксації
def relax(a, b, e):
    m = min(abs(d_f(a)), abs(d_f(b)))
    M = max(abs(d_f(a)), abs(d_f(b)))
    print("RELAX")

    x0 = (a + b) / 2.0
    x1 = x0 - 2/(m+M)*f(x0)

    n = math.trunc(math.log(abs(a - x0) / e) / math.log((M + m) / (M - m))) + 1
    print("апріорна оцінка {0}".format(n))

    print(f"{0:3}|{round(x0, 5):10}|{round(f(x0), 5):10}")
    i = 1
    print(f"{i:3}|{round(x1, 5):10}|{round(f(x1), 5):10}")
    x2 = x1 - 2/(m+M)*f(x1)
    while abs((x2 - x1) / (1 - (x2 - x1) / (x1 - x0))) >= e:
        i += 1
        x0 = x1
        x1 = x1 - 2/(m+M)*f(x1)
        x2 = x1 - 2 / (m + M) * f(x1)
        print(f"{i:3}|{round(x1, 5):10}|{round(x0 - x1, 5):10}")
    print(f"{i+1:3}|{round(x2, 5):10}|{round(x1 - x2, 5):10}")


a = 3
b = 5
e = 0.0001

bisection(a, b, e)
print("--------------------------")
simle_iteration(a, b, e)
print("--------------------------")
relax(a, b, e)
print("git")

