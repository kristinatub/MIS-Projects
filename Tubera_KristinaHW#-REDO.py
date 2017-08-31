#Author: Kristina Tubera
#Homework Number & Name: Homework 3
#Due Date:2/13/17
#Program Description:Making a menu

#fromula
pizza_count=0
sides_count=0
pizza=0
sides=0

#print menu
print("Menu Items     Prices")
print("1.Pizza      $7.29sm $12.39 lg")
print()
print("Toppings")
print("2.Green peppers $1.50")
print("3. Mushrooms    $1.50")
print("4.Pepperoni     $2.00")
print("5.Complete my order")

#promt user for name and order
name=input("What is your name?")
order=input("What would you like to order?")

# if statements for mistakes or for nothing ordered
while order < "1" or order>"5":
    print("Invalid. Try again.")
    order=input("What would you like to order?")
if order=="5":
    print("Nothin was purchased.Thanks bye!")
    exit()
#while loop for type of food ordered
while order <="5":

    #for ordering pizza
    if order == "1":
        size=input("what size would you like?( type sm or lg)")
        
        # validate size
        if size=="sm" or size=="lg":
            if size=="sm":
                pizza_count+=1
                print("You just bought a small pizza")
                pizza=pizza+7.29
                order=input("What else would you like to order?")
            elif size=="lg":
                pizza_count+=1
                print("You just bought a large pizza")
                pizza=pizza+12.39
                order=input("What else would you like to order?")
                            
        #mark invalid if size is wrong
        elif size!="sm" or size!="lg":
            print("invalid order. Try again.( type sm or lg)")
            
     # for ordering topping       
    elif order == "2":
        sides_count+=1
        sides=sides+1.50
        print("You ordered Green Peppers")
        order=input("What else would you like to order?")
        
    # for ordering mushrooms
    elif order == "3":
        sides_count+=1
        sides=sides+1.00
        print("You ordered Mushroom")
        order=input("What else would you like to order?")

    #for ordering pepperoni
    elif order == "4":
        sides_count+=1
        sides=sides+2.00
        print("You ordered pepperoni")
        order=input("What else would you like to order?")
        
#print receipt
    elif order=="5":
        total_price=float(sides+pizza)
        total_tax=float(total_price*.0825)
        total_amount=float(total_price*1.0825)
        print()
        print(name)
        print("Total number of pizzas ordered:",pizza_count)
        print("Total number of topings ordered:",sides_count)
        print("Price before tax:$",end=''"%.2f"%total_price)
        print()
        print("Sales tax:$", end=''"%.2f"%total_tax)
        print()
        print("Total amount due:$",end=''"%.2f"%total_amount)
        exit()
        
