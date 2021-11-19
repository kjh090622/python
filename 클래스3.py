class money:
    def __init__(self,num,won):
      self.num = num
      self.won = won
 
    def __gt__(self,other):
        return self.won > other.won

def maxsearch(sav):
    king = sav[0]

    for now in sav:
        if now > king:
            king = now
    return king

saving = []


for i in range(5):
    won = int(input("%d번 저축금액은?:"%(i+1)))
    saving.append(money(i+1, won))

king = maxsearch(saving)

print("저축왕 %d번 %d원 축하합니다"%(king.num,king.won))
    
