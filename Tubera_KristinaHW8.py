#Author: Kristina Tubera
#Homework Number: Homework 8 
#Due Date: April 10 2017
#Program description: OOP
import cellphoneusage

#define constants
UPDATE_INFO=1
MAKE_CALL=2
SEND_TEXTS=3
VIEW_CURRENT_USAGE=4
FINALIZE_BILL=5
#define main
def main():
    menu()
    #create object
    cell=cellphoneusage.CellPhoneUsage()
    answer=get_user_input()

    #account info
    while answer<FINALIZE_BILL:
        
        #update name and number
        if answer==UPDATE_INFO:
            name=str(input("what is the account name?"))
            cell.set_account_name(name)
            print()
            new_account_number=change_account_num()
            cell.set_account_num(new_account_number)
            print()
            answer=get_user_input()
            
        #update minutes
        if answer==MAKE_CALL:
            minutes=int(input("How many minutes was your call?"))
            cell_minutes=cell.make_call(minutes)
            while cell_minutes==False:
                print("Invalid.Please try again.")
                minutes=int(input("How many minutes was your call?"))
                cell_minutes=cell.make_call(minutes)
            print()
            answer=get_user_input()
            
        #update texts   
        if answer==SEND_TEXTS:
            text=int(input("How many texts did you send?"))
            cell_texts=cell.send_texts(text)
            while cell_texts==False:
                print("Invalid.Please try again.")
                text=int(input("How many texts did you send?"))
                cell_texts=cell.send_texts(text)            
            print()
            answer=get_user_input()
            
        # see usage          
        if answer==VIEW_CURRENT_USAGE:
            usage=cell.__str__()
            print(usage)
            print()
            answer=get_user_input()
            
    #print all info        
    if answer==FINALIZE_BILL:
        cell.display_bill()

#def menu
def menu():
    print("CELL PHONE PLAN USAGE:\n1. Update account info\n2. Make call\n3. Send texts\n4. View current usage\n5. Finalize bill")
    
#define get user input
def get_user_input():
    choice=int(input("what would you like to do?"))
    while choice>5 or choice<1:
        print("invalid. Try again")
        choice=int(input("what would you like to do?"))
    return choice

#define change account number
def change_account_num():
    num=input("What should we change the acct num to?")
    return num

main()


    
    
    
