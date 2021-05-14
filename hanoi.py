def hanoi(n, source, destination, temp):
    if n == 1:
        print(source, 'to', destination)
    else:
        hanoi(n-1, source, temp, destination)
        print(source, 'to', destination)
        hanoi(n-1, temp, destination, source)


hanoi(8, 0, 2, 1)