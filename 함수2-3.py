def inp():
    global a,b
    a = int(input("숫자를 입력하세요 : "))
    b = int(input("숫자를 입력하세요 : "))

def sort():
    global x,y
    x = max(a,b)
    y = min(a,b)

def gugu():
    for i in range(y,x+1):
        for j in range(1,10):
            print("%d x %d = %d"%(i,j,i*j))
        print()

inp()
sort()
gugu()
