#Author: Kristina Tubera
#Homework Number: Homework 9 
#Due Date: April 19 2017
#Program description: Inheritance
#import plain burger
import plainburger

#define constants
CHEESE=.99
BACON=1.79
AVOCADO=1.99

#create class
class DeluxeBurger(plainburger.PlainBurger):
    def __init__(self,name,qty,size):
        super().__init__(name,qty,size)
        self.__cheese=True
        self.__bacon=True
        self.__avocado=True
        
    #define get cheese
    def get_cheese(self):
        return self.__cheese

    #defineget_bacon
    def get_bacon(self):
        return self.__bacon

    #define get avocado
    def get_avocado(self):
        return self.__avocado
    
    #define remove cheese
    def remove_cheese(self):
        self.__cheese= False

    #define remove bacon
    def remove_bacon(self):
        self.__bacon= False

    #define remove avocado
    def remove_avocado(self):
        self.__avocado= False

    # define calc cost
    def calc_cost(self):
        total=0
        amount=self.get_qty()
        cost=self.get_price()
        if self.__cheese==True:
            total+=CHEESE
        if self.__bacon==True:
            total+=BACON
        if self.__avocado==True:
            total+=AVOCADO

        total_cost=(amount*cost)+(amount*total)

        return total_cost
    def __str__(self):
        #get total
        total=self.calc_cost()

        # get quantity
        amount=self.get_qty()

        #get size
        size=self.get_size()

        #get cheese result
        cheese=self.get_cheese()

        #get bacon result
        bacon=self.get_bacon()

        #get avocado result
        avocado=self.get_avocado()
        
        # calculate the different options and combinations for food
        if (cheese== True) and (bacon== True) and (avocado== True):
            
            var = str(amount) + "deluxe Burger "+ size + " Toppings: cheese bacon avocado $ " +str(format(total,'.2f'))
        elif (cheese == True) and (bacon== False) and (avocado== False):
            var = str(amount) + " deluxe Burger "+ size + " Toppings: cheese $ "  +str(format(total,'.2f'))
        elif (cheese == False) and (bacon == False) and (avocado== False):
            var = str(amount) + " deluxe Burger "+ size + " 0 Toppings $ "  +str(format(total,'.2f'))

        elif (cheese == False) and (bacon == True) and (avocado== False):
            var = str(amount) + " deluxe Burger "+ size + " Toppings: bacon $ "  +str(format(total,'.2f'))
        elif (cheese== True) and (bacon== True) and (avocado== False):
            var = str(amount) + " deluxe Burger "+ size + " Toppings: cheese bacon $ "  +str(format(total,'.2f'))

        elif (cheese == False) and (bacon == False) and (avocado== True):
            var = str(amount) + " deluxe Burger "+ size + " Toppings: avocado $ " +str(format(total,'.2f'))
       
        elif (cheese == True) and (bacon == False) and (avocado== True):
            var = str(amount) + " deluxe Burger "+ size + " Toppings: cheese avocado $ " +str(format(total,'.2f'))
        elif (cheese== False) and (bacon == True) and (avocado == True):
            var = str(amount) + " deluxe Burger "+ size + " Toppings: bacon avocado $ "+str(format(total,'.2f'))
               
        return var
        
