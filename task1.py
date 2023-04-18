class Cat:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def meow(self):
        print(f"{self.name} мяукнул!")

    def purr(self):
        print(f"{self.name} мурлыкает...")

    def sleep(self):
        print(f"{self.name} спит... zzz...")

my_cat = Cat("Барсик", "рыжий", 3)
print(f"Имя: {my_cat.name}")
print(f"Окрас: {my_cat.color}")
print(f"Возраст: {my_cat.age}")
my_cat.meow()
my_cat.purr()
my_cat.sleep()