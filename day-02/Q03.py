'''Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.'''

print("----GCD/HCF Calculation----")

num = int(input("Enter the first num: "))
num2 = int(input("Enter the second num: "))

limit = min(num, num2)

for i in range(limit, 0, -1):
    if num%i == 0 and num2%i == 0 :
        print("GCD: ", i)
        break