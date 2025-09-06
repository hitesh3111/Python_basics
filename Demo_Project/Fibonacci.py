def fibonacci():
    a = 0
    b = 0
    c = 1
    for number in range (0,10):
        a = b
        b = c
        c = a+b
        print(c)


fibonacci()