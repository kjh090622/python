hap = 0
score = list(map(int,input().split()))

for i in range(5):
    hap += score[i]

avg = hap/5

if avg >= 80:
    print("PASS")
else:
    print("FAIL")
