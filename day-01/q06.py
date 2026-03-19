''' 7. Write a program to calculate the electricity bill (accept number of unit from user) according 
to the following criteria : 
Unit                                                     
First 100 units                                               
Next 100 units                                              
After 200 units                                             
Price   
no charge 
Rs 5 per unit 
Rs 10 per unit 
(For example if input unit is 350 than total bill amount is Rs2000) '''


print("----ELECTRICITY BILL CALCULATOR----")
units = int(input("Enter the no. of units used: "))

if units<=100:
    print("No charge")

elif units>=100 and units<200:
    units_new = units-100
    price_initial = units_new * 5
    print("Charge: ", price_initial, " Rs. only/-")

elif units>=200:
    previous_units = 100 * 5
    units_new02 = units - 200
    bill = previous_units + (units_new02*10)
    print("Charge: ", bill, " Rs. only/-")
else:
    print("Invalid input, Please try again.")
