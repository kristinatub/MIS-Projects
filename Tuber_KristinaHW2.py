#Author: Kristina Tubera
#Homework Number: Homework 9
#Due Date: Nov 14 2016
#Program description: Inheritance
#import files
import desserts
import candy
import cookie
import icecream
import sundae
CHOICE_1="CANDY"
CHOICE_2="COOKIE"
CHOICE_3="ICE CREAM"
CHOICE_4="SUNDAE"
#define main
def main():
    desserts_list=[]
    menu()
    choice=get_choice()
    
    while choice==1 or choice==2 or choice==3 or choice==4:
        #get the order
         if choice==1:
             
             name=CHOICE_1
             kind=input("Please enter the kind of dessert(type/flavor):")
             weight=0
             price_pound=0

             candy_class=candy.Candy(name,kind)
             #promt user for more info
             purchase_candy(desserts_list,candy_class)
             choice=get_choice()
         elif choice==2:
             name=CHOICE_2
             quantity=0
             price_dozen=0
             kind=input("Please enter the kind of desert(type,flavor):")
             cookie_class=cookie.Cookie(name,kind)
             #promt user for more info
             purchase_cookie(desserts_list,cookie_class)
                          
             choice=get_choice()
         elif choice==3:
             name=CHOICE_3
             size=""
             kind=input("Please enter the kind of desert(type,flavor):")

             icecream_class=icecream.Icecream(name,kind)
             #promt user for more info
             purchase_ice_cream(desserts_list,icecream_class)
             choice=get_choice()
         elif choice==4:
             name=CHOICE_4
             toppings=0
             sundae_class=sundae.Sundae(name,toppings)

             #promt user for more info
             purchase_sundae(desserts_list,sundae_class)
        
             choice=get_choice()
        
    if choice==5:
             print("Thank you for stopping by!")
     
             count=0
             for num in desserts_list:
                 count=count+1
             print("Number of desserts purchased is:",count)
             
            
    
             
#define menu    
def menu():
    print("Dessert Menu\n 1. Candy\n2. Cookie\n3. Ice Cream\n4. Sundae\n5. Exit")
#define get_choice    
def get_choice():
    choice=int(input( "what would you like to order?"))
    while choice<=0 or choice>=6:
        print("Error. try again!")
        choice=int(input( "what would you like to order?"))
    return choice
#define purcahse candy
def purchase_candy(desserts_list,candy_class):
    weight=float(input("Please enter weight (in pounds):"))
    value=candy_class.update_weight(weight)
    while value==False:
        weight=float(input("Please enter weight (in pounds):"))
        value=candy_class.update_weight(weight)
                      
    price_pound=float(input("Please enter price per pound:"))                      
    value=candy_class.update_price_per_pound(price_pound)
    while value==False:
        weight=float(input("Please enter price per pound):"))
        value=candy_class.update_price_per_pound(price_pound)
    desserts_list.append(candy_class)

  
#define purcahse cookies    
def purchase_cookie(desserts_list,cookie_class):
    quantity=int(input("Please eneter quantity of cookies"))
    value=cookie_class.update_quantity(quantity)
    while value==False:
        quantity=float(input("Please enter weight (in pounds):"))
        value=cookie_class.update_quantity(quantity)

    price_dozen=int(input("Please eneter price per dozen"))
    value=cookie_class.update_price_per_dozen(price_dozen)
    while value==False:
        price_dozen=float(input("Please enter price per dozen"))
        value=cookie_class.update_quantity(price_dozen)

    desserts_list.append(cookie_class)
   
     
#define purchase ice cream        
def purchase_ice_cream(desserts_list,icecream_class):

    size=str(input("Please enter size (S, M, or L)"))
    value=icecream_class.update_size(size)
    while value==False:
        size=str(input("Please enter size (S, M, or L)"))
        value=icecream_class.update_size(size)
    

    icecream_class.update_price(size)
    
   
    desserts_list.append(icecream_class)
    
    
#define purchase sundae
def purchase_sundae(desserts_list,sundae_class):
    toppings=int(input("Please enter amount of toppings"))
    value=sundae_class.update_toppings(toppings)
    while value==False:
        toppings=float(input("Please enter amount of toppings"))
        value=sundae_class.update_toppings(toppings)
             
                             
    
   
    desserts_list.append(sundae_class)


#call main       
main()                  
                      
