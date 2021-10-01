import random

print("가위바위보를 게임을 시작합니다")

while True:
    computer = random.choice(['가위','바위','보'])
    player = input("무엇을 낼래?")

    if computer == '가위':
        print("컴퓨터 : 가위")
        if player == '가위':
            print("플레이어 : 가위")
            print("무승부")
        elif player == '바위':
            print("플레이어 : 바위")
            print("플레이어 승")
        elif player == '보':
            print("플레이어 : 보")
            print("컴퓨터 승")

    elif computer == '바위':
        print("컴퓨터 : 바위")
        if player == '가위':
            print("플레이어 : 가위")
            print("컴퓨터 승")
        elif player == '바위':
            print("플레이어 : 바위")
            print("무승부")
        elif player == '보':
            print("플레이어 : 보")
            print("플레이어 승")

    elif computer == '보':
      print("컴퓨터 : 보")
      if player == '가위':
            print("플레이어 : 가위")
            print("플레이어 승")
      elif player == '바위':
            print("플레이어 : 바위")
            print("컴퓨터 승")
      elif player == '보':
            print("플레이어 : 보")
            print("무승부")


      q = input("더 할거야? Y/N")
      if q == 'Y' or q == 'y':
          continue
      else:
          print("프로그램 종료")
          break
