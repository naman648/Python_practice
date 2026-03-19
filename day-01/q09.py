''' 10. Write a program to accept the price of a bike and display the road tax and 
insurance to be paid according to the following criteria . also display total amount to 
be paid. 
Cost price (in Rs)           Tax                Insurance                             
> 100000                     15%                    20%       
> 50000 and <= 100000        10%                    8%
<= 50000                      5%                    5%         
'''

print("----TAX CALCULATOR BASIC----")
price = int(input("Enter the price of the bike: "))

if price>100000:
    new_price = (price * (115/100)) + (price * (120/100))
    print("Total amount to be paid: ", new_price)

elif price > 50000 and price <= 100000:
    new_price02 = (price * (110/100)) + (price * (108/100))
    print("Total amount to be paid: ", new_price02)

elif price <= 50000:
    new_price03 = (price * (105/100)) + (price * (105/100))
    print("Total amount to be paid: ", new_price03)

else:
    print("Invalid input, Please try again.")

