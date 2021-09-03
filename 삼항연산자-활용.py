num1 = int(input("정수를 입력하세요."))
num2 = int(input("정수를 입력하세요."))
num3 = int(input("정수를 입력하세요."))

max_data = num1 if num1 > num2 else num2
max_data = num3 if num3 > max_data else max_data

print("최댓값:%d"%max_data)
