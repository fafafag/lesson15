class Good:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
        self.cost = self.calc()

    def calc(self):
        return self.price * self.weight

apple = Good('apple', price = 100, weight = 1.5)
pear = Good('pear', price = 120, weight = 0.8)

print(apple.cost)
print(pear.cost)