import random

brand = random.choice(["BMW", "Mercedes", "Nissan", "Audi", "Toyota", "Chevrolet"])

def model():
    if brand == "BMW":
        model = random.choice(["i5", "M5", "i8"])
    elif brand == "Mercedes":
        model = random.choice(["EQE", "Glc", "AMG EQE sedan"])
    elif brand == "Nissan":
        model = random.choice(["GT-R", "Skyline", "Z"])
    elif brand == "Audi":
        model = random.choice(["r6", "A6", "A1"])
    elif brand == "Toyota":
        model = random.choice(["Camry", "RAV4", "Corolla"])
    else:
        model = random.choice(["Camaro", "Corvette", "Impala"])

model()

class Human:
    def __init__(self, name="Human"):
        self.name = name
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.driver = []
    def add_driver(self, *args):
        for driver in args:
            self.driver.append(driver)
    def print_driver(self):
        if self.driver != []:
            print(f"Ім'я водія, що їде в {self.brand, self.model}")
            for driver in self.driver:
                print(driver.name)
        else:
            print(f"Автомобіль {self.brand, self.model} порожній")

Oleksiy = Human("Oleksiy")
Sofia = Human("Sofia")
Artem = Human("Artem")

car1 = Car(brand, model)
car1.add_driver(Oleksiy)

car2 = Car(brand, model)
car2.add_driver(Sofia)

car3 = Car(brand, model)
car3.add_driver(Artem)

print(car1.driver, car1.brand, car1.model)
print(car2.driver, car2.brand, car2.model)
print(car3.driver, car3.brand, car3.model)