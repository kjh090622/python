"""
1부터 12사이의 정수를 입력받아 입력받은 월의 날수를
출력하는 프로그램
"""
num = int(input("달을 입력하세요"))
if num == 1 or num == 3 or num == 5 or num == 7 or num == 8 or num == 10 or num == 12:
          print("%d월 31일입니다"%num)
elif num == 4 or num == 6 or num == 9 or num == 11:
          print("%d월 30일입니다"%num)
elif num == 2:
          print("%d월 28일입니다"%num)
else:
    print("잘못 입력하셨습니다")
                
