import random

class Student:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.25
        self.gladness -= 3

    def to_sleep(self):
        print("Time to sleep")
        self.gladness += 3

    def to_chill (self):
        print("Resting time")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("You failed your exams")
            self.alive = False
        elif self.gladness <= -10:
            print("Depression")
            self.alive = False
        elif self.progress > 10 and self.gladness <= 15:
            print("You passed your exams, but are you happy?")
        elif self.progress > 10 and self.gladness >= 15:
            print("You passed your exams, and you ARE happy")
        else:
            print("You got sent for a second year")

    def end_of_day(self):
        print(f"Gladness is {self.gladness}")
        print(f"Progress is {self.progress}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        vibir = random.randint(1, 3)
        if vibir == 1:
            self.to_study()
        elif vibir == 2:
            self.to_sleep()
        elif vibir == 3:
            self.to_chill()
        self.is_alive()
        self.end_of_day()

You = Student(name = "Oleksiy", age = random.randint(12, 14), height = random.randint(158, 175), weight = random.randint(40, 55))
print("Your name is " + You.name)
print("You're", You.age, "years old")
print("You're height is'", You.height, "cm tall")
print("You weight", You.weight, "kg")

for day in range(365):
    if You.alive == False:
        break
    You.live(day)