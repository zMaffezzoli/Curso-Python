for i in range(1000, 10000):

    if ((int(str(i)[:2]) + int(str(i)[2:]))**2) == i:
        print(i)