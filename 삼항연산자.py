"""
삼항연산자.py
삼항연산자를 이용하여 두 수 중 작은 값 출력
"""
num1 = int(input("정수를 입력하세요.")) 
num2 =int(input("정수를 입력하세요."))

min_data = num2 if num1 > num2 else num1
print("최솟값:%d"%min_data)
