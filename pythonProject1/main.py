if __name__ == '__main__':
    a = int(input())
    maximum = a
    while a != 0:
        if maximum > a:
            maximum = a
        a = int(input())
        print(maximum)


