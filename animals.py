# Name : Augustine Mwangi
# Date : 23/02/2026

# Program to show inheritance in python


class Animal():
    def __init__(self,species,weight,food)
        self.species = species
        self.weight = weight
        self.food = food

    def grow(self,weight)
        weight = 1.1* weight
        print(f"The animal weighs {weight} in kgs")

    def eat(self,food)
        print(f"The animal eats{food}")



class Dog(Animal):
    def __init__(self,colour,weight,breed)
        super().__init(species,weight,food)
        self.colour = colour
        self.weight = weight
        self.breed = food

    def grow(self,weight)
        weight = 1.1* weight
        print(f"The animal weighs {weight} in kgs")

    def barks(self ):
        print(f"The dog says woof woof")

class Horse(Animal):
    def __init__(self,species,weight,food)
        self.species = species
        self.weight = weight
        self.food = food

    def grow(self,weight)
        weight = 1.1* weight
        print(f"The animal weighs {weight} in kgs")

    def neighs(self ):
        print(f"The horse says neigh neigh")
        
