class Charactaristics:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        pass

class Hero(Charactaristics):
    def __init__(self, name, health, weaponizers):
        super().__init__(name, health)
        self.weaponizers = weaponizers

    def attack(self):
        print(f"{self.name} attacks with {self.weaponizers}")

class Enemy(Charactaristics):
    def __init__(self, name, health, damagizers):
        super().__init__(name, health)
        self.damagizers = damagizers

    def attack(self):
        print(f"{self.name} attacks with {self.damagizers}")

hirou = Hero("Heroinic Oleksiji", 125, "Inverted spear of Heaven")
hirou.attack()

enemistics = Enemy("Evil Artemiji", 75, 25)
enemistics.attack()
