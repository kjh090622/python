"""
나이를 입력받아 20살 이상이면 An adult
그렇지 않으면 몇년후에 성인이 되는지
()years라는 메세지를 메세지를 출력하는 프로그램
""" 
age = int(input("나이를 입력해주세요"))
if age >= 20:
    print("An adult")
else:
    print("%d years" %(20 - age))
