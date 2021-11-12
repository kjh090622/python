class GoldFishBread:
    def make_Gold(self, ingredients, price):
        self.ingredients = ingredients
        self.price = price


    def see_Gold(self):
        print(self.ingredients, self.price)

a = GoldFishBread()
b = GoldFishBread()

a.make_Gold('팥', 30000)
b.make_Gold('슈크림',30000)


a.see_Gold()
b.see_Gold()










