for b in range(10):
    for a in range(b + 1):
        print('#', end=' ')
    for a in range(10 - b):
        print(' ', end=' ')
    for a in range(10 - b):
        print('#', end=' ')
    for a in range(10 - b):
        print(' ', end=' ')
    for a in range(7 - 1):
        print(' ', end=' ')
    for a in range(b + 1):
        print('*', end=' ')
    for a in range(10 - b):
        print('*', end=' ')
    for a in range(6 - b):
        print('*', end=' ')
    for a in range(5 + b):
        print(' ', end=' ')
    for a in range(b + 1):
     print('#', end=' ')
    print()
