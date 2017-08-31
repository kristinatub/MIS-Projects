#Author: Kristina Tubera
#Homework Number: Final Project
#Due Date: May 10 2017
#Program description: Final Project


#create class
class Student():

    #define init
    def __init__(self,new_id,new_fname,new_lname,classes):
        self.__uteid=new_id
        self.__fname=new_fname
        self.__lname=new_lname
        self.__class_list=classes

    #define get uteid
    def get_uteid(self):
        return self.__uteid

    #define get fname
    def get_fname(self):
        return self.__fname

    #define get lname
    def get_lname(self):
        return self.__lname

    #define get classes
    def get_classes(self):
        return self.__class_list

    #define add class
    def add_class(self,unique_num):
        class_list=self.__class_list

        #if else statment to see if you can remove class
        if unique_num not in class_list:
            self.__class_list.append(unique_num)

            #return true if you can add student to class
            print("The student was added to the class. Unique number is "+unique_num)
            return True
        elif unique_num in class_list:

            #return false if you cant add it in
            print("The student was already enrolled in the class with unique number:" +unique_num+". Try another course.")
            return False

    #define drop class    
    def drop_class(self,unique_num):
        class_list=self.__class_list

        #if else statement to see if you can remove 
        if unique_num in class_list:
            self.__class_list.remove(unique_num)

            #return true if you can remove
            return True
        elif unique_num not in class_list:

            #return false if you cant remove
            print("The student cannot be dropped from a class he is not enrolled in. Try another class other than: "+unique_num)
            return False

    #define line for file
    def line_for_file(self):
        eid=self.__uteid
        fname=self.__fname
        lname=self.__lname
        class_list=self.__class_list

        #create line
        line=(eid+':'+fname+':'+lname+':'+str(':'.join(class_list))+'\n')

        return line

    #define str
    def __str__(self):
        eid=self.__uteid
        fname=self.__fname
        lname=self.__lname
        class_list=self.__class_list
        
        #fix var       
        var=eid+' '+fname+' '+lname+' \n'
        for x in class_list:
            var+=str(x)+'\n'

        #return var    
        return var
            
        
        
