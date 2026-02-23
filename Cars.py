# Name : Augustine Mwangi
# Date : 23/02/2026

# Program to show classes in python

class Car():
    # attributes of the car
    def __init__(self, model, make, colour, year):
        self.model = model
        self.make = make
        self.colour = colour
        self.year = year

    # Print car details
    def print_details(self,model,make,colour,year):
        print(f"{make} {model} of colour {colour} was manufactured in the year {year}")



#Instantiate a class object

my_car = Car("Maybach", "Mercedes Benz", "Black", "2024")
dads_car = Car("Land Cruiser", "Toyota", "White", "2022")

my_car.print_details("Maybach", "Mercedes Benz", "Black", "2024")






