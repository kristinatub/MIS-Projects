#Author: Kristina Tubera
#Homework Number: Homework 9 
#Due Date: April 19 2017
#Program description: Inheritance

#import entree
import entree

#define constants
TOPPINGS=.99
PIZZA_PRICE=1.99

#create class
class PizzaSlice(entree.Entree):

    #define init
    def __init__(self, name, qty, toppings):
        super().__init__(name,qty)
        self.__toppings= toppings

    #define get toppings
    def get_toppings(self):
        return self.__toppings

    #define calc cost
    def calc_cost(self):
        pizza_amount=self.get_qty()
        toppings_amount=self.get_toppings()
        
        cost=(int(toppings_amount)*pizza_amount*TOPPINGS)+(pizza_amount*PIZZA_PRICE)
        return cost

    #define str
    def __str__(self):
        total=self.calc_cost()
        var= str(self.get_qty()) +" Pizza slice " +str(self.__toppings)+" Toppings $"+ str(format(total,'.2f'))
        return var
    
        
