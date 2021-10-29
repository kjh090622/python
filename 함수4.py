def average(a,b,c):
  
 
  hap = kor + eng + mat
  avg = hap/3
  return avg

kor,eng,mat = map(int,input("세 과목의 점수를 입력하세요:"). split())
avg = average(kor,eng,mat)
print("평균:%2f"%avg)
