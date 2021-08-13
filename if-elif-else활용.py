"""
if-elif-else 활용.py
복싱 체급 프로그램
몸무게를 입력받아 체급을 출력하는 프로그램
몸무게가 50.8kg이하 - Flyweight
63.23kg이하 - Middleweight
88.45이하 - Cruiserweight
그 이상은 Heavtweight
"""
print("복싱체급안내 프로그램입니다")
print("====================")
weight = float(input("몸무게를 입력해세요"))
if weight < 0
    print("잘못입력했습니다")
    exit()
if weight <= 50.8:
    print("Flyweight")
elif weight <= 63.23:
    print("Middleweight")
elif weight <= 88.45:
    print("Cruiserweight")
else:
    print("Heavyweight")
    
