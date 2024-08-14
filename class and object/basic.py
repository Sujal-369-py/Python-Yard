class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

my__car = Car("toyoto","Corolla")
print(my__car.brand)
print(my__car.model)
print(my__car.full_name())

my_new_car = Car("BMW","I7")
print(my_new_car.full_name())