#Creating a program using polymorphism 
class Animal():

    def speak(self):
        print("Animal makes a Sound")

class Dog(Animal):

    def speak(self):
        print("Dog Barks")

class Cat(Animal):
    
    def speak(self):
        print("Cat Meows")

class Cow(Animal):

    def speak(self):
        print("Cow Moo")

animals=[Dog(),Cat(),Cow()]
for animal in animals:
    animal.speak()
