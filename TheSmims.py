import random

class Human:
    def __init__(self, name="Human"):
        self.name = name
        self.money = 1000
        self.gladness = 25
        self.hunger = 40
        self.home = Home()
        self.car = Car()
        self.job = Job()

    def eat(self):
        if self.home.food <= 0:
            self.shopping("Buy food")
        self.hunger = min(100, self.hunger + 20)
        self.home.food -= 10
        print("You ate")

    def work(self):
        if not self.car.drive():
            print("Car repair")
            self.car.repair()
            self.money -= 500
        else:
            print("Driving to your office...")
            print("You're working")
            self.money += self.job.salary
            self.gladness -= 5
            self.hunger -= 15
    
    def chill(self):
        print("Resting")
        self.gladness += 5
        self.home.mess += 5
        self.hunger -= 10
    
    def mess_home(self):
        print("Cleaning the mess...")
        self.home.mess = 0
        self.gladness -= 5
        self.hunger -= 5
    
    def shopping(self, type):
        if type == "Buy food":
            print("Buying food")
            self.money -= 200
            self.home.food += 50
        elif type == "Fuel":
            print("Fueling")
            self.money -= 75
            self.car.fuel += 50
    
    def is_alive(self):
        if self.hunger <= 0:
            print("You died of hunger")
            return False
        elif self.gladness <= 0:
            print("Depression")
            return False
        elif self.money <= 500:
            print("'My mom is kinda homeless'"
                  "Too many debts")
            return False
        return True

    def day_life(self, day):
        print(f"\n ====={self.name}'s day {day} of life=====")
        print(f"Money: {self.money} Hunger: {self.hunger} Gladness: {self.gladness}")

        if self.hunger < 15: self.eat()
        elif self.gladness <= 15: self.chill()
        elif self.car.fuel < 5: self.shopping("Fuel")
        elif self.home.mess > 15: self.clean.home()
        else:
            random.choice([self.eat, self.work, self.chill])()

class Car:
   def __init__(self):
       self.fuel = 50
       self.strength = 40
   def drive(self):
       if self.fuel > 5 and self.strength > 5:
           self.fuel -= 5
           self.strength -= 1
           return True
       return False
   def repair(self):
       self.strength += 35
class Job:
    def __init__(self):
        self.salary = random.randint(50, 150)
class Home:
    def __init__(self):
        self.food = 20
        self.mess = 0

Oleksiy = Human("Oleksiy")
for day in range(1, 8):
    if not Oleksiy.is_alive():
        break
    Oleksiy.day_life(day)