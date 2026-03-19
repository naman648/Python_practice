''' Write a program to check whether an years is leap year or not 
the year is leap if it satisfies following condition 
• It the year is divisible by 100 
o If it is divisible by 100, then it should also be divisible by 400 then it is 
leap year 
• otherwise, all other years divisible by 4 and not divisible by 100 then it is leap 
year. '''

print("----LEAP YEAR FINDER----")

year = int(input("Enter the year: "))

if year%100==0 and year%400==0 or year%4==0: 
    print("It's a LEAP Year.")
else:
    print("Not a LEAP Year.") 

