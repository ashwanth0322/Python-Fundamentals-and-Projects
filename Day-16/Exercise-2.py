#Creating a Vehicle management system 
class Vehicle():

    def __init__(self,brand,colour,year):
        self.brand=brand
        self.colour=colour
        self.year=year

    def display_info(self):
        print("Brand Name :",self.brand)
        print("Colour :",self.colour)
        print("Year :",self.year)

class Car(Vehicle):

    def __init__(self,brand,colour,year,model_type):
        super().__init__(brand,colour,year)
        self.model_type=model_type

    def display_info(self):
         super().display_info()
         print("Model Type :",self.model_type)

class bike(Vehicle):

    def __init__(self, brand, colour, year,number_of_gears):
        super().__init__(brand, colour, year)
        self.number_of_gears=number_of_gears

    def display_info(self):
        super().display_info()
        print("Number Of Gears :",self.number_of_gears)

car1=Car("Tesla","Black",2026,"Sedan")
car1.display_info()
bike1=bike("Royal Enfield","Silver",2024,6)
print()
bike1.display_info()