'''Write a program in python to display the sum of the series
[ 1+x+x^2/2!+x^3/3!+....]. Go to the editor (H.P.)
Test Data :
Input the value of x :3
Input number of terms : 5
Expected Output :
The sum is : 16.375000'''

import math

x = float(input("Enter the value of x: "))
n = int(input("Enter the no. of terms: "))

total = 0

for i in range(n):
    total = total + (x ** i) / math.factorial(i)  # x ** i means x to the power of i

print(f"The sum is: {total: .6f}")  # upto 6 digits after point or decimal of float

