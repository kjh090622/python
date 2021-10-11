hap = 0
score = list(map(int,input().split()))

for i in range(5):
    hap += score[i]

avg = hap/5

print('총점:%d점'%hap)
print('평균:%.1f점'%avg)
