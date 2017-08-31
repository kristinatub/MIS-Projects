#Author: Kristina Tubera
#Homework Number & Name: Homework 7
#Due Date:10/24/16
#Program Description:Organizing IROM

#DECLARE CONSTANTS
DATA_FILE="StudentData.txt"
MIS_304="MIS304.txt"
MIS_325="MIS325.txt"

VIEW_BOTH=1
VIEW_EITHER_OR_BOTH=2
VIEW_304=3
VIEW_325=4
VIEW_ONE=5
ENROLL_STUDENT=6
ADD_STUDENT=7
DROP_STUDENT=8
UPDATE_STUDENT=9
EXIT=10

#define main
def main():
    #Display menu
    print_menu()
    
    #create empty sets and lists
    name_dict={}
    email_dict={}
    mis_304_set=set()
    mis_325_set=set()

    #input information into sets and lists
    create_dictionaries1(name_dict,email_dict)
    create_sets(mis_304_set,mis_325_set)

    #promt user for choice
    menu=get_choice()



    while menu!=EXIT:
        #get info for students taking both MIS classes
        if menu==VIEW_BOTH:
            print('\n'+"Students Taking BOTH MIS 304 and MIS 325:")
            all_set=mis_304_set.intersection(mis_325_set)
            #for loop to print out name and e-mail
            for name in all_set:
                real=name_dict[name]
                e_mail=email_dict[name]
                #function to print name
                print_name(real,e_mail)
                                              
            print("Number of Students Taking Both is: "+str(len(all_set)))
            print()
            #promt user for menu option
            menu=get_choice()
            
        #get info for students taking either or both MIS classes           
        elif menu==VIEW_EITHER_OR_BOTH:
            both=mis_304_set.union(mis_325_set)
            print('\n'+"Students Taking EITHER or BOTH MIS 304 and MIS 325:")
            for name in both:
                real=name_dict[name]
                e_mail=email_dict[name]
                #function to print name
                print_name(real,e_mail)
                
            print("Number of Students Taking Either or Both is: "+str(len(both)))
            #promt user for menu option
            menu=get_choice()
            
        #get info for students taking MIS304    
        elif menu==VIEW_304:
            mis304=mis_304_set.difference(mis_325_set)
            print('\n'+"Students Taking MIS 304:")
            for student in mis304:
                real=name_dict[student]
                e_mail=email_dict[student]
                #function to print name
                print_name(real,e_mail)
                
            print("Number of Students Taking 304 is: "+str(len(mis304)))
            print()
            #promt user for menu option
            menu=get_choice()
            
        #get info for students taking MIS325                
        elif menu==VIEW_325:
            mis325=mis_325_set.difference(mis_304_set)
            print('\n'+"Students Taking MIS 325:")
            for student in mis325:
                real=name_dict[student]
                e_mail=email_dict[student]
                #function to print name
                print_name(real,e_mail)

            print("Number of Students Taking MIS325 is: "+str(len(mis325)))
            #promt user for menu option
            menu=get_choice()
        #get info for students taking only one class
        elif menu==VIEW_ONE:
            only_one=mis_325_set.symmetric_difference(mis_304_set)
            print('\n'+"Students Taking one MIS class:")
            for student in only_one:
                real=name_dict[student]
                e_mail=email_dict[student]
                #function to print name
                print_name(real,e_mail)

            print("Number of Students Taking one MIS class is: "+str(len(only_one)))
            #promt user for menu option
            menu=get_choice()
            
        #Enroll a new student   
        elif menu==ENROLL_STUDENT:
            get_id=add_student()
            get_name=get_name_from_user()
            new_email=create_email(get_name)
            
            

            name_dict[get_id]=get_name
            email_dict[get_id]=new_email
            
            #promt user for menu option
            menu=get_choice()
            
        #add an already enrolled student into a class    
        elif menu==ADD_STUDENT:
            get_student=add_student()
            if get_student not in name_dict:
                print("Student not found. Try again.")
                get_student=add_student()
            get_class=add_class()

            if get_class=="1":
                mis_304_set.add(get_student)
            
            else:
                mis_325_set.add(get_student)
                
            #promt user for menu option
            menu=get_choice()
            
         # drop a student from a class                           
        elif menu==DROP_STUDENT:
            remove_student=remove()
            while remove_student not in name_dict:
                    print("please try again")
                    remove_student=remove()
            leave_class=remove_class()

            if leave_class=="1":
                mis_304_set.remove(remove_student)
            else:
                mis_325_set.remove(remove_student)
            #promt user for menu option
            menu=get_choice()
            
        #update the information of an already enrolled student           
        elif menu==UPDATE_STUDENT:
            
            
            type1=input("choose 1 to update e-mail choose 2 to update name")
            
            if type1=='1':
                
                get_ied=add_student()
                while get_ied not in name_dict:
                    print("please try again")
                    get_ied=add_student()
                type3=input("Please enter e-mail address.")
                if '@' not in type3:
                    print("Need an @ sign. Please try again.")
                    type3=input("Please enter e-mail address.")
                email_dict[get_ied]=type3
                menu=get_choice()
                
            else:
            
                get_ied=add_student()
                while get_ied not in name_dict:
                    print("please try again")
                    get_ied=add_student()
                name2=input("Please enter name.")
                name_dict[get_ied]=name2
                menu=get_choice()
                
        else:                
            print("Wrong choice. Try again.")
            menu=get_choice()
    
#define create_email
def create_email(got_name):
    e_mail=got_name.split()
    name1=e_mail[0]
    name2=e_mail[1]
    new_email=(name1+name2+'@utexas.edu')
    return new_email

 #define print_students   
def print_name(real1,e_mail1):
    print((real1)+' ('+e_mail1+')'+'\t') 
    
#define remove_clas
def remove_class():
    class_type= input("What class would you like to be removed from? 1= MIS 304. 2=MIS 325")

    return class_type

#define remove()
def remove():
    name=input("What is the eid of the student would you like to remove?")

    return name

#define add_student
def add_student():
    eid=input("What is the eid?")
    num_list=['1','2','3','4','5','6','7','8','9']
    letter_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #validate ied
    while (eid[0] in num_list) or (eid[1] in num_list) or (eid[2] in num_list) or (eid[3] in letter_list) or (eid[4] in letter_list )or (eid[5] in letter_list):
        eid=input("Bad eid. Try again. What is the eid?")                 
    
    return eid

#define add_class
def add_class():
    class2=input("What class would you like to be added to? 1= MIS 304. 2=MIS 325")
    
    
    return class2
    
#define get_name_from_user   
def get_name_from_user():
    name=input("what is your name?")
    name_list=list(name)
    #validate name
    while ' ' not in name_list:
        name=input("Put a space between your name. what is your name?")
        name_list=list(name)
        
    return name

#define print_menu    
def print_menu():
    print("Please choose an option.")
    print("1. Which students take both MIS 304 and MIS 325?")
    print("2. Which students are taking either or both MIS classes?")
    print("3. Which students are taking MIS 304 but not MIS 325?")
    print("4. Which students are taking MIS 325 but not MIS 304?")
    print("5. Which students take one MIS class but not both?")
    print("6. Enroll a new student in the MIS program")
    print("7. Add a student to an MIS class")
    print("8. Drop a student from an MIS class")
    print("9. Update a student's email address")
    print("10. Exit")
    
#define create_dictionaries1
def create_dictionaries1(names_dict,emails_dict):
    student_info_file=open(DATA_FILE,'r')
    

    for student in student_info_file:
        student_list=student.split()
        ied=student_list[0]
        first_name=student_list[1]
        last_name=student_list[2]
        email=student_list[3].rstrip('\n')

    
        names_dict[ied]=first_name+' '+last_name
        emails_dict[ied]=email
        
#define create sets
def create_sets(mis_304,mis_325):
    
    student_info_file2=open(MIS_304,'r')
    student_info_file3=open(MIS_325,'r')
    
    for mis in student_info_file2:
        mis_304.add(mis.rstrip('\n'))
        
    for mis in student_info_file3:
        mis_325.add(mis.rstrip('\n'))
        
#define get_choice       
def get_choice():
    choice=int(input("What would you like to do?"))
    
    #validate user input
    while choice<=0 and choice>=11:
        choice=int(input("What would you like to do?"))
    return choice       

main()
