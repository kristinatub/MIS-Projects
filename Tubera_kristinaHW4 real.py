
#promt user for name and order
def main():
    menu()
    ordernumber1=0
    ordernumber2=0
    ordernumber3=0
    ordernumber4=0
    ordernumber5=0
    ordernumber6=0
    ordernumber7=0
    count=0
    sentinel=8
    name= input("What is your name?")
    ordernumber= int(input("What do you want"))
    ordernum(ordernumber)
    

def menu():
    print("GRAPEFRUIT ELECTRONICS\r1. gPod $249\r2. gPad Pro $599\r3. gPhone 7 Plus $769\r4. gMac $1,499\r5. gMacBook Pro $1,999\r6. gMac Pro $2,999\r7. Grapefruit Watch $299\r8. Complete order")

# if statements for mistakes or for nothing ordered
def ordernum(ordernumber):
    if ordernumber==8:
        print("Thank you for shopping. Bye!")
        exit()

    while ordernumber>=9:
        print("Invalid order try again")
        ordernumber= float(input("What would you like to order ( Type 1,2,3,4 or 5 to finish)? "))

    #while loop for type of order ordered
    while ordernumber ==1 or ordernumber==2 or ordernumber==3 or ordernumber==4 or ordernumber==5 or ordernumber==6 or ordernumber==7:
        
        if ordernumber==1:
        
            count= float(input("How many would you like?"))
            while count<=0:
                print("invalid order. Numberc annot be negative or zero:")
                count= float(input("How manypwould you like?"))
            item1=count*249
            total_count=total_count+count
            ordernumber= float(input("What else would you like to order?"))
            while ordernumber>=9:
                print("Invalid order try again")
                ordernumber= float(input("What else would you like to order?"))
        elif ordernumber==2:
            count= float(input("How many would you like?"))
            while count<=0:
                print("invalid order. Numberc annot be negative or zero:")
                count= float(input("How manypwould you like?"))
            item1=count*599
            total_count=total_count+count
            ordernumber= float(input("What else would you like to order?"))
            while ordernumber>=9:
                print("Invalid order try again")
                ordernumber= float(input("What else would you like to order?"))
        elif ordernumber==3:
            
            count= float(input("How many would you like?"))
            while count<=0:
                print("invalid order. Numberc annot be negative or zero:")
                count= float(input("How manypwould you like?"))
            item1=count*769
            total_count=total_count+count
            ordernumber= float(input("What else would you like to order?"))
            while ordernumber>=9:
                print("Invalid order try again")
                ordernumber= float(input("What else would you like to order?"))
        elif ordernumber==4:
            
            count= float(input("How many would you like?"))
            while count<=0:
                print("invalid order. Numberc annot be negative or zero:")
                count= float(input("How manypwould you like?"))
            item1=count*1499
            total_count=total_count+count
            ordernumber= float(input("What else would you like to order?"))
            while ordernumber>=9:
                print("Invalid order try again")
                ordernumber= float(input("What else would you like to order?"))
        elif ordernumber==5:
            
            count= float(input("How many would you like?"))
            while count<=0:
                print("invalid order. Numberc annot be negative or zero:")
                count= float(input("How manypwould you like?"))
            item1=count*1999
            total_count=total_count+count
            ordernumber= float(input("What else would you like to order?"))
            while ordernumber>=9:
                print("Invalid order try again")
                ordernumber= float(input("What else would you like to order?"))
        elif ordernumber==6:
            
            count= float(input("How many would you like?"))
            while count<=0:
                print("invalid order. Numberc annot be negative or zero:")
                count= float(input("How manypwould you like?"))
            item1=count*299
            total_count=total_count+count
            ordernumber= float(input("What else would you like to order?"))
            while ordernumber>=9:
                print("Invalid order try again")
                ordernumber= float(input("What else would you like to order?"))
        elif ordernumber==7:
            
            count= float(input("How many would you like?"))
            while count<=0:
                print("invalid order. Numberc annot be negative or zero:")
                count= float(input("How manypwould you like?"))
            item7=count*299
            total_count=total_count+count
            ordernumber= float(input("What else would you like to order?"))
            while ordernumber>=9:
                print("Invalid order try again")
                ordernumber= float(input("What else would you like to order?"))
            while food>=6:
                print("Invalid order try again")
                ordernumber=float(input("What would you like to order? "))
            
    if discount(total_count):
        
        total_count=total_count
        total=ordernumber1+ordernumber2+ordernumber3+ordernumber4+ordernumber5+ordernumber6+ordernumber7
      
        if total_count>15:
            discount_total+=(total_count*total*.25)
            print("Discount total is:", discount_total)
        elif total_count in range(10,16):
            discount_total=total_count*total*.2
            print("Discount total is:", discount_total)
        elif count in range(5,10):
            discount_total=total_count*total*.1
            print("Discount total is:", discount_total)
        elif total_count<5:
            print("No discount")                       
                    

    if ordernumber==8:
    #print receipt
        total_count=total_count
        total=item1+item+item3+item4+item5+item6+item7
        discounted_price=total-discount_total
        sales_tax=total*.0825
        total_with_tax=total*1.0825
        print()
        print("Name:", name)
        print("Total Price: $",end='' "%.2f"% total)
        print()
        print("Total quantity of electronics", total_count)
        print("Discount total is:", discount_total)
        print("Discounted price is:",discounted_price)
        print("Sales Tax: $",end='' "%.2f"% sales_tax)
        print()
        print("Total due is: $",format(total_with_tax, '.2f'))
            

main()
          
   



