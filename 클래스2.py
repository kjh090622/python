class GoldFishBread:
    def make_Gold(self, ingredients, price):
        self.ingredients = ingredients
        self.price = price
    def see_Gold(self):
        print(self.ingredients, self.price)

    def __add__(self,other):
        return self.price + other.price

a = GoldFishBread()
b = GoldFishBread()

a.make_Gold('팥',300)
b.make_Gold('슈크림',400)

print('붕어빵 두개에 %d원'%int(a+b))




