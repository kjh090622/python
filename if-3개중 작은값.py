num1 = int(input("정수를 입력하세요."))
num2 = int(input("정수를 입력하세요."))
num3 = int(input("정수를 입력하세요."))
if num1 > num2:
        min_data = num2
        if min_data > num3:
                min_data = num3
else:
        min_data = num1
        if min_data > num3:
                min_data = num3
print("최솟값:%d"%min_data)
