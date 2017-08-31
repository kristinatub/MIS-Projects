#Author: Kristina Tubera
#Homework Number & Name: Homework 5
#Due Date:3/5/17
#Program Description:Calculate Averages

#DECLARE CONSTANTS
EMPLOYEES_NAMES="Employees-3weeks.txt"
EMPLOYEES_NAMES_AND_AVERAGES="EmployeesAverages.txt"



SENTINEL=0

def main():
    file_found = True  #Was the input file found
    good_data = True   #Was good data read from the file
                #set count to zero
    count=0

    try:
        employees_input=open(EMPLOYEES_NAMES, 'r')

    except FileNotFoundError:
        
        print("Could not find", INPUT, "in the current directory.")
        file_found = False
    if file_found:
        
        employees_output=open(EMPLOYEES_NAMES_AND_AVERAGES ,'w')
        first=employees_input.readline().rstrip("\n")
        last=employees_input.readline().rstrip("\n")

        
        while first!=''and last!='':
            try:
                
                            #get weeks    
                number_of_hour=get_hour_number()
            
            #validate number of weeks
                number_of_hour=hour_validation(number_of_hour)
            
            except exception as Err:
                print("Could not convert end weight to int")
                good_data = False
            if good_data:
        
                #calculate average
                countgrade=0
                for student in range(number_of_hour):
                    first=employees_input.readline().rstrip("\n")
                    last=employees_input.readline().rstrip("\n")
                    grade=int(employees_input.readline().rstrip('\n'))
                    countgrade+=grade
                    average=get_average(number_of_hour,countgrade)
                    
                        
                    #count number of people
                    count=count+1
                    
                    #print data to file
                    print_to_file(employees_output,first,last,average)
                    first=employees_input.readline().rstrip('\n')
                    last=employees_input.readline().rstrip('\n')
                
    employees_input.close()
    employees_output.close()
    print("Number of employees:",count)
    print("Output File name:",EMPLOYEES_NAMES_AND_AVERAGES)

    

#define get_week_number       
def get_hour_number():
    number_of_hour=int(input("How many weeks did each employee work?"))
    
    return number_of_hour
#define week_validation
def hour_validation(number_hour):
    while number_hour<=SENTINEL:
        print("Invalid order. Please try again.")
        number_hour=int(input("How many weks did each employee work?"))

    return number_hour
#define get_average
def get_average(number_hour,count_grade):
    average=count_grade/number_hour
    return average
def print_to_file(file,first_name,last_name,average_all):
    file.write(str(last_name)+', '+str(first_name)+" "+str(format(average_all,".2f"))+ "\n")
main()
   
    
                  
                               
