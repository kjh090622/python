cur_temp = 20

def set_temp(temp):
    global cur_temp

    if (cur_temp <temp):
        while (cur_temp < temp):
          cur_temp += 1
          print("현재 온도는 %d도입니다"%cur_temp)
    else:
      while(cur_temp > temp):
          cur_temp -= 1
          print("현재 온도는 %d도입니다"%cur_temp)


print("에어컨을 자가동시키니다")

while True:
  put_temp = input("원하는 온도를 입력해주세요 :")

  if(put_temp == '종료'):
    print("에어컨을 종료합니다")
    break
  elif(put_temp<='50'and put_temp >= '-50'):
      print("현재 온도는 %d도 입니다"%cur_temp)
      set_temp(int(put_temp))
  else:
      print("다시 입력하세요")




