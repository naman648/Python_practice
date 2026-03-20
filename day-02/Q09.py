'''Write a program in python to find the sum of the series
[ x - x^3 + x^5 + ......]. Go to the editor (H.P.)
Test Data :
Input the value of x :2
Input number of terms : 5
Expected Output :
The values of the series:
2
-8
32
-128
512
The sum = 410 '''

x = float(input("Enter the value of x: "))
n = int(input("Enter the no. of terms: "))

total = 0

print("The values of the series:")

for i in range(n):
    power = 2 * i + 1              # generates 1,3,5,7,...
    term = x ** power             # x^1, x^3, x^5,...

    if i % 2 != 0:                # alternate sign
        term = -term

    print(int(term))              # printing each term
    total = total + term

print(f"The sum = {int(total)}")