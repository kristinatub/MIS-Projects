#Author: Kristina Tubera
#Homework Number & Name: Homework 7
#Due Date:3/27/17
#Program Description:Organizing Data

#DECLARE CONSTANTS
OUT_FILE="Pizza-output.txt"
OUT_FILE2="Salad-output.txt"
PIZZA_FILE="Pizza.txt"
SALAD_FILE="Salad.txt"

VIEW_BOTH=1
VIEW_EITHER_OR_BOTH=2
VIEW_PIZZA=3
VIEW_SALAD=4
VIEW_ONE=5
MOST_PIZZA=6
MOST_SALAD=7
LEAST_PIZZA=8
LEAST_SALAD=9
EXIT=10

def main():
    #print menu function
    print_menu()

    pizza_dict={}
    salad_dict={}
    pizza_set=set()
    salad_set=set()

    #create dictionaries
    create_dictionaries(pizza_dict,PIZZA_FILE)
    create_dictionaries(salad_dict,SALAD_FILE)

    #create sets
    create_sets(pizza_set,OUT_FILE)
    create_sets(salad_set,OUT_FILE2)
    
    #print info into an output file
    put_into_output(pizza_dict,salad_dict)

    #promt user for choice
    menu=get_choice()

    #while loop for all my info

    while menu != EXIT:
        #view both
        if menu==VIEW_BOTH:
            both=pizza_set.intersection(salad_set)
            print('\n'+"Customers who got BOTH Pizza and Salad:")
            print_set(both)               
            print()
            menu=get_choice()
         #view either           
        elif menu==VIEW_EITHER_OR_BOTH:
            either=pizza_set.union(salad_set)
            print('\n'+"Customers who got Either or BOTH Pizza and Salad:")
            print_set(either)
            print()
            menu=get_choice()
                
                   
        elif menu==VIEW_PIZZA:
            pizza=pizza_set.difference(salad_set)
            print('\n'+"Customer who got only Pizza:")
            print_set(pizza)               
            print()
            menu=get_choice()
            
        elif menu==VIEW_SALAD:
            salad=salad_set.difference(pizza_set)
            print('\n'+"Customer who got only Salad:")
            print_set(salad)               
            print()
            menu=get_choice()

        elif menu==VIEW_ONE:
            print()
            only_one=pizza_set.symmetric_difference(salad_set)
            print('\n'+"Customer who got only one:")
            print_set(only_one)               
            print()
            menu=get_choice()
            
        elif menu==MOST_PIZZA:
            print()
            print("Who Purchased the most pizza?")
            best_item=best_item_function(pizza_dict)
            print(best_item[0]+' bought'+' '+str(best_item[1])+' '+"pizza(s).")
            print()
            menu=get_choice()
                
        elif menu==MOST_SALAD:
            print()
            print("Who Purchased the most salads?")
            best_item=best_item_function(salad_dict)
            print(best_item[0]+' '+'bought'+' '+str(best_item[1])+' '+"salad(s).")
            print()
            menu=get_choice()

        elif menu==LEAST_PIZZA:
            print()
            print("Who Purchased the least pizza?")
            least_item=least_item_function(pizza_dict)
            print(least_item[0]+' '+'bought'+' '+str(least_item[1])+' '+'pizza(s).')
            print()
            menu=get_choice()
            
        elif menu==LEAST_SALAD:
            print()
            print("Who Purchased the least salad?")
            least_item=least_item_function(salad_dict)
            print(least_item[0]+' '+'bought'+' '+str(least_item[1])+' '+'salad(s).')
            print()
            menu=get_choice()
    else:
        print("Thanks!")

    
#def put into output file
def put_into_output(dict1, dict2):
    pizza_output=open(OUT_FILE,'w')
    salad_output=open(OUT_FILE2,'w')
    for key in dict1:
        pizza_output.write((key+' '+str(dict1[key]))+'\n')
    for key in dict2:
        salad_output.write((key+' '+str(dict2[key]))+'\n')
    pizza_output.close
    salad_output.close

#define best items   
def best_item_function(dictionary):
    best=max(dictionary.values())
    for key,number in dictionary.items():
        if best==number:
            best=(key,best)
    return best

#define least item 
def least_item_function(dictionary1):
    least=min(dictionary1.values())
    for key,number in dictionary1.items():
        if least==number:
            least=(key,least)
    return least
#print menu   
def print_menu():
    print("Customer Analysis.")
    print("1. Which customers got Both Pizza and salad?")
    print("2. Which customers are taking either or both Pizza and salad?")
    print("3. Which customers are taking Pizza but not Salad?")
    print("4. Which customers are taking salad but not pizza?")
    print("5. Which customers take one but not both?")
    print("6. Most pizza")
    print("7. Most salad")
    print("8. LEast Pizza")
    print("9. Least Salad")
    print("10. Exit")

#print name
def print_set(set1):
    for name in set1:
        print(name)
    print("There are "+str(len(set1))+" customers.")
    

#define create dictionary
def create_dictionaries(dict1,file):
    file1=open(file,'r')
    
    for customer in file1:
        customer_info=customer.rstrip('\n').split()
        fname=customer_info[0].lower().title()
        lname=customer_info[1].lower().title()
        name=(fname+' '+lname)

        if name in dict1:
            dict1[name]+=1
        else:
            dict1[name]=1
    file1.close()

#define create set
def create_sets(set1,file):
    
    file1=open(file,'r')
    
    
    for pizza in file1:
        customer_info=pizza.rstrip('\n').split()
        fname=customer_info[0].lower().title()
        lname=customer_info[1].lower().title()
        name=(fname+' '+lname)
        set1.add(name)
        

#define get choice
def get_choice():
    choice=int(input("What would you like to do?"))
    
    
    #validate user input
    while choice<=0 or choice>=11:
        print("Invalid choice try again.")             
        choice=int(input("What would you like to do?"))
    return choice

#define main
main()
 

    
        
        
        
        
    
    
