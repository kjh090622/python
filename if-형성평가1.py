num1 = int(input("정수를 입력하세요."))
num2 = int(input("정수를 입력하세요."))
if num1 > num2:
         result = num1 - num2  
else:
         result = num2 - num1

print("정답:%d"%result)

result = (num1 - num2) if num1 > num2 else num2 - num1
print("정답:%d"%result)
