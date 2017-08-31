#Author: Kristina Tubera
#Homework Number & Name: Homework 1
#Due Date:9/5/16
#Program Description: Code for total revenue, total cost, quantity sold, and percentage profit for a product

#promt user for product name
product_name= input("Please enter product name: ")

#promt user for product price
product_price= input("Please enter product's price: $")

#promt user for product cost
product_cost= input("Please enter product's cost: $")

#promt user for quantity sold
quantity_sold= input("Please enter quantity of the product sold: ")

# convert strings into float
product_price= float(product_price)
product_cost= float(product_cost)
quantity_sold= float(quantity_sold)


#calculate total revenue      
total_revenue=product_price*quantity_sold

#calculate total cost
total_cost=product_cost*quantity_sold

#calculate total profit
total_profit=(product_price-product_cost)*quantity_sold

#calculate percentage profit
percentage_profit=(total_profit/(product_price*quantity_sold))*100

#print everything
print()
print("product_name:", product_name)
print("total_revenue: $",end=''"%.2f"% total_revenue)
print()
print("total_cost: $",end=''"%.2f"% total_cost)
print()
print("quantity_sold: ",end=''"%.0f"% quantity_sold)
print()
print("total_profit: $",end=''"%.2f"% total_profit)
print()
print("percentage_profit:","%.2f"% percentage_profit,end=''"%")


