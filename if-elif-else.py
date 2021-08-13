"""
if-elif-else개념. py
elif : else if의 줄임말
if조건:
    실행문1
elif조건:
    실행문2
elif조건:
    실행문3
else:
    실행문4
입력받은 점수를 "수우미양가"평가하는
프로그램
수: 90이상 100이하
우:80이상90미만
미:70이상 80미만
양:60이상 70미만
가:60미만

if조건에서 조건이 두개일때
2개 다 참이여야만 실행 - 교집합(and)
1개만 참이어도 실행 - 합집합(or)
"""
score = int(input("점수를 입력하세요"))
if score > 100 or score < 0 :
    print("잘못입력하셨습니다")
    exit()
if score >= 90:
    print("수")
elif score >= 80:
    print("우")
elif score >= 70:
    print("미")
elif score >= 60:
    print("양")
else:
    print("가")

