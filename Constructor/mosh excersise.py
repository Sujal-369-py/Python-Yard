class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print("Hi I am ",self.name," and what about you")


sujal = Person("Sujal")
sujal.talk()

sanu = Person("Sanu")
sanu.talk()