#Author: Kristina Tubera
#Homework Number: Final Project
#Due Date: May 10 2017
#Program description: Final Project


#import files
import course
import student

#create constants
ADD_COURSE=1
DROP_COURSE=2
PRINT_STUDENT_SCHEDULE=3
PRINT_COURSE_SCHEDULE=4
DONE=5

STUDENT_FILE='students.txt'
COURSE_FILE='courses.txt'

STUDENT_OUTPUT='students-updated.txt'
COURSES_OUTPUT='courses-updated.txt'


#define maint
def main():

    #create dictionaires
    student_dict={}
    course_dict={}

    #process both files
    process_student_file(STUDENT_FILE,student_dict)
    process_course_file(COURSE_FILE,course_dict)

    #print menu and get choice
    print_menu()
    choice=get_choice()

    
    #while loop for options other than 5
    while choice != DONE:
        if choice==ADD_COURSE:

            #get id andcourse
            eid=get_id(student_dict)
            course_id=get_unique_number(course_dict)
            
            #create course object
            course_object=course_dict[course_id]

            #see if space available
            space_available=course_object.space_available()
        
    

            #while loop for space not available
            while space_available == False:
                print("There is not space available in that class. Choose another class.")
                course_id=get_unique_number(course_dict)
                course_object=course_dict[course_id]
                space_available=course_object.space_available()
                course_object.calc_seats_remaining()
                
            # check to see if student is in class if there is space
            student_object=student_dict[eid]
            student_in_class=student_object.add_class(course_id)

            #while loop to see if student is already in class
            while student_in_class == False:
                course_id=get_unique_number(course_dict)
                student_in_class=student_object.add_class(course_id)

            #enroll student    
            course_object.enroll_student()

            
            #print menu and get choice
            print_menu()
            choice=get_choice()

        #elif for option two    
        elif choice==DROP_COURSE:

            #get id and course
            eid=get_id(student_dict)
            course_id=get_unique_number(course_dict)

            #create student object
            student_object=student_dict[eid]
            
            class_list=student_object.drop_class(course_id)

            #while loop to see if student can be dropped from course
            while class_list == False:
                course_id=get_unique_number(course_dict)
                class_list=student_object.drop_class(course_id)

            #if True then drop student from course and drop the class from student
            student_object.drop_class(course_id)
            course_object=course_dict[course_id]
            course_object.drop_student()

            #calculate seats remaining
            course_object.calc_seats_remaining()
                
            #print menu and get choice    
            print_menu()
            choice=get_choice()

        #choice for option 3    
        elif choice==PRINT_STUDENT_SCHEDULE:

            #get id andcourse
            eid=get_id(student_dict)

            #send to print student info function
            print_student_info(student_dict,eid,course_dict)

            #print menu and get choice 
            print_menu()
            choice=get_choice()

        # choice for option 4    
        elif choice==PRINT_COURSE_SCHEDULE:

            #send to print course schedule function
            print_course_schedule(course_dict)

            #print menu and get choice
            print_menu()
            choice=get_choice()
            
    #explain option 5           
    if choice==DONE:
        
        #write to file
        write_to_output(student_dict,STUDENT_OUTPUT)
        write_to_output(course_dict,COURSES_OUTPUT)
        print("Bye!")
        exit()

#define write to output
def write_to_output(dictionary1,output_file1):

    #output file
    output=open(output_file1, 'w')

    #for loop to print acutal names of classes even though its not necessary but conley said I could keep it
    for key in dictionary1:
        generic_object=dictionary1[key]
        output_line=generic_object.line_for_file()
        output.write(output_line+'\n')

    #close file    
    output.close()
    

#define print menu
def print_menu():
    print("1. Add course")
    print("2. Drop course")
    print("3. Print student's schedule")
    print("4. Print course schedule")
    print("5. Done")

#define get choice
def get_choice():

    #prompt user for choice
    choice=int(input("What would you like to do?"))
    
    
    #validate user input
    while choice<=0 or choice>=6:
        print("Invalid choice try again.")             
        choice=int(input("What would you like to do?"))
    return choice

#define process student file
def process_student_file(student_file1,student_dict1):
    
    #open file
    file1=open(student_file1,'r')

    #for loop to set the contents in the file into the dictionary
    for name in file1:
        student_info=name.rstrip('\n').split(':')
        uteid=student_info[0]
        fname=student_info[1]
        lname=student_info[2]

        #create empty set
        classes=[]

        #for loop to collect the classes
        for x in range(3,len(student_info)):
            classes.append(student_info[x])

            
         # create student object                  
        student1=student.Student(uteid,fname,lname,classes)    

        #put all into dictionary
        student_dict1[uteid]=student1
    return student_dict1
    
#define process course file        
def process_course_file(course_file1,course_dict1):

    #open file
    file1=open(course_file1,'r')

    #for loop to set the contents in the file into the dictionary
    for name in file1:
        course_info=name.rstrip('\n').split(';')
        unique=course_info[0]
        title=course_info[1]
        prof=course_info[2]
        seats_taken=int(course_info[3])
        capacity=int(course_info[4])
        

        course1=course.Course(seats_taken)
        course1.set_unique(unique)
        course1.set_title(title)
        course1.set_prof(prof)
        course1.set_capacity(capacity)

        #put all into dictionary
        course_dict1[unique]=course1
    return course_dict1
#define get id    
def get_id(student_dict1):
    eid=input("what is the eid of the student you want to view?")

    #while loop to validate
    while eid not in student_dict1:
        eid=input("Invalid eid "+eid+". What is the eid of the student you want to view?")
    return eid

#define get unique number
def get_unique_number(course_dict1):
    unique_number=input("What is the unique number?")

    #while loop to validate
    while unique_number not in course_dict1:
        unique_number=input("Invalid.What is the unique number?")
    return unique_number
#define student info       
def print_student_info(student_dict1,eid1,course_dict1):

    #call on student object to get all the information
    student_object=student_dict1[eid1]
    class_list=student_object.get_classes()
    
    #print student info
    print(str(student_object))

    #loop to name off real title of class
    for x in class_list:
        class_name=x
        real_name=course_dict1[class_name]
        title=real_name.get_title()
        print(title+'\n')
    
#define print ourse schedule    
def print_course_schedule(course_dict1):

    #for loop to print info
    for key in course_dict1:
        print(course_dict1[key])
        

#call mainc
main()    
