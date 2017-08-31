import icecream
class Sundae (icecream.Icecream):
    #define attributes
    def __init__(self,name,kind):
        super().__init__(name,kind)
        self.__toppings=0
    #return toppings
    def get_toppings(self):
        return self.__toppings
    #update toppings
    def update_toppings(self,new_toppings):
        if new_toppings <= 0:
            return False
        if new_toppings > 0:
            self.__toppings = new_toppings
            return True
    #calculate cost
    def calculate_cost(self):
        total=self.__toppings * .29
    #print all
    def __str__(self):
        var=(str(self.__toppings))
        return var
