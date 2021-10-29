def star(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end='')
        print()

n = int(input("입력해주세요"))
star(n)
