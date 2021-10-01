print("계산기입니다")
while True:
    print("숫자를 입력하세요")
    a = int(input("a: "))
    b = int(input("b: "))
    print("a+b = %d"%(a+b))

    c = input("종료하시겠습니까? Y/N: ")
    if c == 'Y' or c == 'y':
        print("프로그램을 종료합니다")
        break
