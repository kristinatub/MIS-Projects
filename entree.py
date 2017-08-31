#Author: Kristina Tubera
#Homework Number: Homework 9 
#Due Date: April 19 2017
#Program description: Inheritance

#create entree
class Entree():

    #define init
    def __init__(self,start_name,start_qty):
        self.__name=start_name
        self.__quantity=start_qty

    # define get name
    def get_name(self):
        return self.__name

    #define get quantity
    def get_qty(self):
        return self.__quantity

    # define str
    def __str__():
        var="Item:" +self.__name+\
            "Quantity: "+str(self.__quantity)
        
