import random
import time


words= ["꿇땋잋풑챁탙","풑착랓터", "문재앙", "그거 그렇게 하는거 아닌데", "마춥뻠 좀 틀리지 마세여", "앛밓훛탑핲리햏앜랕랲"]

n = 1
print("준비되면 엔터")
input()
start = time.time()
q = random.choice(words)

while n <= 5:
    print("*문제:",n)
    print(q)
    x = input()
    if q == x:
        print("통과")
        n += 1
        q = random.choice(words)
    else:
        print("오타입니다")


end = time.time()
et = end-start
