import desserts
class Icecream (desserts.Desserts):
    #define attributes
    def __init__(self,name,kind):
        super().__init__(name,kind)
        self.__size=""
        self.__price=0
    #return size
    def get_size(self):
        return self.__size
    #update size
    def update_size(self,new_size):
        self.__size=new_size
       
    #return price
    def get_price(self):
        return self.__price
    #update price
    def update_price(self,size):
            if self.__size == "S":
                self.__price=1.49
            elif self.__size=="M":
                self.__price=1.99
            else:
                self.__price=2.49
            return True
    #define calculate cost
    def calculate_cost(self):
        total = self.__price * self.__size
       
        return total
    #print all
    def __str__(self):
        var=(str(self.__size)+str(self.__price))
        return var
    


