I=int(input("enter level of the pyramid:"))


def pyramid(I):
    for i in range(I):
        print(' ' * (I - i - 1) + '*' * (2 * i + 1))

10
pyramid(I)

    