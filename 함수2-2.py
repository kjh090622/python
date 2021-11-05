def inp():
    global a,b
    a = int(input('수를 입력 :'))
    b = int(input('수를 입력 :'))


def calc():
    global hap, gob
    hap = a+b
    gob = a*b

def outp():
    print("합 : ",hap)
    print("곱 : ",gob)

inp()
calc()
outp()
