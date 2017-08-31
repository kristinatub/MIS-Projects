#Author: Kristina Tubera
#Homework Number: Final Project
#Due Date: May 10 2017
#Program description: Final Project

#create class
class Course():
    #define init
    def __init__(self,seats_taken):
        self.__unique='unique'
        self.__title='title'
        self.__prof='prof'
        self.__seats_taken=seats_taken
        self.__capacity=0

    # define get unique
    def get_unique(self):
        return self.__unique

    #define set unique
    def set_unique(self,new_unique):
        self.__unique=new_unique

    #define get_title    
    def get_title(self):
        return self.__title

    #define set_title
    def set_title(self,new_title):
        self.__title=new_title

    #define get_prof
    def get_prof(self):
        return self.__prof

    #define set prof
    def set_prof(self,new_prof):
        self.__prof=new_prof

    #define get seats taken    
    def get_seats_taken(self):
        return self.__seats_taken

    #defien get capacity
    def get_capacity(self):
        return self.__capacity

    #define set capacity
    def set_capacity(self,new_capacity):
        self.__capacity=new_capacity

    #calculate seats remaining
    def calc_seats_remaining(self):
        taken=self.__seats_taken
        capacity=self.__capacity

        #formula for remaining seats
        remaining=capacity-taken

        return remaining

    #define space available
    def space_available(self):
        remaining=self.calc_seats_remaining()

        #if else statement for remaining
        if remaining > 0:
            return True
        elif remaining==0:
            return False

    #define enroll student    
    def enroll_student(self):
    
        #add one to seats taken
        self.__seats_taken+=1

    #define drop student
    def drop_student(self):
        

        #delete seats taken
        self.__seats_taken +=1

    #define line for file
    def line_for_file(self):

        #call attributes
        unique=self.__unique
        title=self.__title
        prof=self.__prof
        seats_taken=self.__seats_taken
        capacity=self.__capacity

        #create line
        line=(str(unique)+';'+title+';'+prof+';'+str(seats_taken)+';'+str(capacity)+'\n')
        return line

    #define str    
    def __str__(self):
        unique=self.__unique
        title=self.__title
        prof=self.__prof
        calc_seats_remaining1=self.calc_seats_remaining()
        var=unique+' '+title+' '+prof+' '+str(calc_seats_remaining1)

        #return var
        return var
        
        
    
