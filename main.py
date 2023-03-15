import random

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.happiness = 50
        self.hunger = 50
        self.alive = True

    def play(self):
        print(f"{self.name} wants to play!")
        self.happiness += 10
        self.hunger += 5

    def eat(self):
        print(f"{self.name} is hungry and needs to eat.")
        self.hunger -= 10

    def sleep(self):
        print(f"{self.name} is tired and needs to sleep.")
        self.happiness += 5

    def is_alive(self):
        if self.hunger < 0:
            print(f"{self.name} has starved to death.")
            self.alive = False
        elif self.happiness <= 0:
            print(f"{self.name} has died of sadness.")
            self.alive = False

    def end_of_day(self):
        print(f"{self.name} has {self.hunger} hunger and {self.happiness} happiness.")

    def live(self, day):
        day = f"Day {day} of {self.name}'s life"
        print(f"{day:=^50}")

        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.play()
        elif live_cube == 2:
            self.eat()
        elif live_cube == 3:
            self.sleep()
        self.end_of_day()
        self.is_alive()


cat = Pet(name="Fluffy", species="cat")
for day in range(365):
    if cat.alive == False:
        break
    cat.live(day+1)



