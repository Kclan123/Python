def Race(n):
    if n<=0:
        print("Go")
    else:
        print(n)
        Race(n-1)

Race(5)

