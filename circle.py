#Class header
PI = 3.14
#Class definition
class Circle:
    #Define init function/method
    def __init__(self):
        #Declare attributes
        self.__color = "Red"
        self.__radius = 4.0
        self.__border = 1.0

    def get_border(self):
        return self._border
    
    def set_border(self,new_border):
        if new_border>0:
            self._border=new_border
        
    def get_radius(self):
        return self._radius
    
    def set_radius(self,new_radius):
        if new_radius>0:
            
            self._radius=new_radius
        
    def get_color(self):
        return self._color
    
    def set_color(self,value):
        self._color=value
        
    #Define calc_area
    def calc_area(self):
        area = (self.radius ** 2) * PI
        return area
    
    #Define calc_circumference
    def calc_circumference(self):
        #Calculate circ
        circ = 2 * PI * self.radius
        return circ
                  
