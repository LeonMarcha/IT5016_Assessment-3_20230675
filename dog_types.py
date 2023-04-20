# code from lecturer showing inheritance

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_description(self):
        print(f"{self.name} is aged {self.age} years")

    def get_sound(self):
        print("Bow Bow")

    def getSpecies():
        print(Dog.species)


class CircusDog(Dog):
    def do_tricks(self):
        print("dog is doing tricks")


class LargeDog(Dog):
    def get_sound(self):
        print("Wuff Wuff")


dog1 = Dog("hjgjsa", 10)
dog2 = Dog("hjgjg", 12)

dog3 = CircusDog("CircusDog", 6)

dog3.get_sound()
dog3.do_tricks()

dog4 = LargeDog("LargeDog", 8)

dog4.get_sound()
dog1.get_description()
dog1.get_sound()
Dog.getSpecies()