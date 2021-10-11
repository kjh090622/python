import random

secretNum = random.randint(1,100)
print('1부터 100까지 숫자가 있어요')

for i in range(20):
    print('예상하는 숫자를 입력해주세요')
    guess = int(input('숫자:'))


    if guess < secretNum:
      print('예상한 숫자가 너무 작아요')
    elif guess > secretNum:
      print('예상한 숫자가 너무 커요')
    else:
      break


if guess == secretNum:
  print('승리!정답입니다')
  print('%d번만에 맞혔어요'%(i+1))
else:
    print('패배했습니다, 정답은 %d입니다.'%secretNum)
