import desserts

class Candy (desserts.Desserts):
    #define attributes
    def __init__(self,name,kind):
        super().__init__(name,kind)
        self.__weight=0
        self.__price_per_pound=0
    #return weight
    def get_weight(self):
        return self.__weight
    #update weight
    def update_weight(self,new_weight):
        if new_weight <= 0:
            return False
        if new_weight > 0:
            self.__weight = new_weight
            return True
    #return price per pound
    def get_price_per_pound(self):
        return self.__price_per_pound
    #update price per pound
    def update_price_per_pound(self,new_price):
        if new_price <= 0:
            return False
        if new_price > 0:
            self.__price_per_pound = new_price
            return True
    #define calculate cost
    def calculate_cost(self):
        total = self.__weight * self.__price_per_pound
       
        return total
    #print all
    def __str__(self):
        string=(str(self.__weight)+str(self.__price_per_pound))
        return string
