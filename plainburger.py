#Author: Kristina Tubera
#Homework Number: Homework 9 
#Due Date: April 19 2017
#Program description: Inheritance
#imporant entree
import entree

#define constants
OZ_6=5.99
OZ_8=7.99
OZ_10=9.99

#create class
class PlainBurger(entree.Entree):
    def __init__(self, name, qty, size):
        super().__init__(name,qty)
        self.__size=size
        self.set_price()

    # define get size
    def get_size(self):
        return self.__size

    #define set price
    def set_price(self):
        if self.__size=='6oz':
            self.__price=OZ_6
        if self.__size=='8oz':
            self.__price=OZ_8
        if self.__size=='10oz':
            self.__price=OZ_10

    # define get price
    def get_price(self):
        return self.__price

    #define calc cost
    def calc_cost(self):
        cost=self.get_price()
        amount=self.get_qty()
        
        total=cost*amount
        return total

    #define str
    def __str__(self):
        #calculate quantity
        quantity_plain=self.get_qty()

        #calcuate cost
        cost_plain=self.calc_cost()

        #calculate size
        size_plain=self.get_size()
        
        var= str(quantity_plain)+" Plain Burger "+ size_plain+ ' $ '+ str(format(cost_plain,'.2f'))
        return var
