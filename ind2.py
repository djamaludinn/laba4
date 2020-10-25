if __name__ == '__main__':
    x = int(input("Введите X: "))
    y = int(input("Введите Y: "))
    if x * x * y < x * (y * y):
        maxim = x * (y * y)
    else:
        maxim = x * x * y
    if x - y > x + 2 * y:
        minim = x + 2 * y
    else:
        minim = x - y
    U = maxim ** 2 + minim ** 2
    print(U)
