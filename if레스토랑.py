"""
1번 - 송로버섯
2번 - 푸아그라
3번 - 캐비어
로 정하고 번호를 입력하면 번호에 해당하는
해당번호가 없으면"나는 빡빡이다"라고 출력한다.
주문하세요 : 1 2 3
"""
menu = int(input("무엇을 주문하시겠습니까?"))
if menu == 1:
    print("주문하신 송로버섯 나왔습니다.")
elif menu == 2:
    print("주문하신 푸아그라 나왔습니다.")
elif menu == 3:
    print("주문하신 캐비어 나왔습니다.")
else:
    print("나는 빡빡이다")
drink = int(input("무슨 음료를 주문하시겠습니까?"))
if drink == 1:
    print("주문하신 맥콜 나왔습니다.")
elif drink == 2:
    print("주문하신 전설의 빡빡이탕 나왔습니다.")
elif drink == 3:
    print("주문하신 탈모탄조식 김치찌개 나왔습니다.")
else:
    print("M자 박치기")
    
