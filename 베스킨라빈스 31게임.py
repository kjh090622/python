import random
print("="*20)
print("made by ???")
print("베스킨라빈스 31 게임")
print("="*20)

number = 0
turn = 0
while True:
    if turn == 0:
     p1 = int(input("사용자 : 숫자의 개수를 입력하세요(1~3) : "))
     for _ in range(p1):
       number += 1
       print('사용자:',number)


     turn += 1
     turn %=2


    elif turn == 1:
        p2 = random.randint(1,3)
        for _ in range(p2):
            number += 1
            print("컴퓨터:",number)


        turn += 1
        turn %= 2


    if number >= 31:
        break



if turn == 0:
  print("사용자 승리")
else:
  print("컴퓨터 승리")
