#Author: Kristina Tubera
#Homework Number: Final Project
#Due Date: May 10 2017
#Program description: Final Project
import entree
import pizzaslice
import plainburger
import deluxeburger

#define constants
PIZZA_SLICE=1
PLAIN_BURGER=2
DELUXE_BURGER=3
COMPLETE_ORDER=4
TAX=.0825

entree_list=[]

#define main
def main():
    menu()
    # get choice
    choice=get_choice()
    if choice == COMPLETE_ORDER:
        print("Thank you for stopping by!")
        exit()
        
    #While loop to get order
    while choice!=COMPLETE_ORDER:
        #order pizza
        if choice==PIZZA_SLICE:
            pizza_count=get_quantity()
            toppings_count=int(input("How many toppings would you like?"))
            while toppings_count<0:
                print("Invalid. Try again")
                toppings_count=int(input("How many toppings would you like?"))
            pizza=pizzaslice.PizzaSlice('Pizza',pizza_count,toppings_count)
            
            #add food to list
            entree_list.append(pizza)

            description=pizza.__str__()
            print(description)
            choice=get_choice()
            
        #order burger    
        if choice==PLAIN_BURGER:
            plain_burger_count=get_quantity()
            size=input("What size would you like? (Enter 6oz or 8oz or 10oz)")
            
            #while statement to check size
            while (size != '6oz') and (size != '8oz') and (size != '10oz'):
                print("Invalid.Enter 6oz or 8oz or 10oz")
                size=input("What size would you like? (Enter 6oz or 8oz or 10oz)")
            plain_burger=plainburger.PlainBurger('Plain Burger',plain_burger_count,size)

            #add food to list
            entree_list.append(plain_burger)
            description=plain_burger.__str__()
            print(description)
            choice=get_choice()
        #order deluxe burger
        if choice==DELUXE_BURGER:
            deluxe_burger_count=get_quantity()
            size=input("What size would you like? (Enter 6oz or 8oz or 10oz)")

            # while loop to check size
            while size!='6oz' and size!='8oz' and size!='10oz':
                print("Invalid.Enter 6oz or 8oz or 10oz")
                size=input("What size would you like? (Enter 6oz or 8oz or 10oz)")
            deluxe_burger=deluxeburger.DeluxeBurger('Deluxe Burger',deluxe_burger_count,size)

            # ask user if they want cheese
            cheese=input("would you like Cheese? type Y or N upper case")

            #validate input
            while cheese!= 'Y' and cheese != 'N':
                cheese=input("type Y or N upper case")
            if cheese=='Y':
                deluxe_burger.get_cheese()
            if cheese=='N':
                deluxe_burger.remove_cheese()
                
            # ask user if they want bacon
            bacon=input("would you like Bacon? type Y or N upper case")

            #validate
            while bacon!= 'Y' and bacon!= 'N':
                bacon=input("type Y or N upper case")
            if bacon=='Y':
                deluxe_burger.get_bacon()
            if bacon=='N':
                deluxe_burger.remove_bacon()
                
            # ask user if they want avocado
            avocado=input("would you like Avocado? type Y or N upper case")

            #validate
            while avocado!= 'Y' and avocado!= 'N':
                avocdo=input("type Y or N upper case")
            if avocado=='Y':
                deluxe_burger.get_avocado()
            if avocado=='N':
                deluxe_burger.remove_avocado()
                
            # add food to list
            entree_list.append(deluxe_burger)
            deluxe_description=deluxe_burger.__str__()
            print(deluxe_description)

            choice=get_choice()
    #print invoice        
    if choice==COMPLETE_ORDER:
        get_invoice(entree_list)
        
 #define menu       
def menu():
    print("Entree Menu\n1. Pizza slice\n2. Plain burger\n3. Deluxe burger\n4. Complete order")

#define get choice
def get_choice():
    choice=int(input("What would you like?"))
    while choice > 4 or choice < 1:
        print("Invalid choice. Try again.")
        choice=int(input("What would you like?"))
    return choice

#define get quantity
def get_quantity():
    quantity=int(input("How much would you like?"))
    while quantity<0:
        print("Please order a positive number.")
        quantity=int(input("How much would you like?"))
    return quantity

#define get invoice
def get_invoice(food_list):
    count=0
    total=0
    for obj in food_list:
        money=obj.calc_cost()
        more=obj.get_qty()
        count+=more
        total+=money
    tax=total*TAX
    total_with_tax=total*1.0825

    print("Total Entrees purchased:", count)
    print("Subtotal: $", format(total,'.2f'),sep='')
    print("Tax: $", format(tax,'.2f'),sep='')
    print("Total with Tax: $", format(total_with_tax,'.2f'),sep='')
    
    

main()
    
        
    
