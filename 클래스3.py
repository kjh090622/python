class GoldFishBread:
    def __init__(self,ingredients,price):
        self.ingredients = ingredients
        self.price = price

    def __str__(self):
        return '{}붕어빵,가격 {}원 주세요.'.format(self.ingredients, self.price)

    def __add__(self, other):
      return self.price + other.price

a = GoldFishBread('팥',400)
b = GoldFishBread('슈크림',500)

print(a)
print(b)
print(a+b,'원')
