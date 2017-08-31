import desserts
class Cookie(desserts.Desserts):
    #define attributes
    def __init__(self,name,kind):
        super().__init__(name,kind)
        self.__quantity=0
        self.__price_per_dozen=0
    
    #return quantity    
    def get_quantity(self):
        return self.__quantity
    #update quantity
    def update_quantity(self,new_quantity):
        if new_quantity <= 0:
            return False
        if new_quantity> 0:
            self.__quantity = new_quantity
            return True
    #return price per dozen
    def get_price_per_dozen(self):
        return self.__price_per_dozen
    #update price per dozen
    def update_price_per_dozen(self,new_price):
        if new_price <= 0:
            return False
        if new_price > 0:
            self.__price_per_dozen = new_price
            return True
    #define calculate cost
    def calculate_cost(self):
        total = self.__price * self.__price_per_dozen
       
        return total
    #print all
    def __str__(self):
        var=(str(self.__quantity)+str(self.__price_per_dozen))
        return var


