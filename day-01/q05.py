''' 6. Accept number from user and check whether it is divisible by 5 and 11 
if divisible then display appropriate message. '''

num = int(input("Enter the number: "))

if num%5==0 and num%11!=0:
    print("Divisible by 5 not 11.")

elif num%5!=0 and num%11==0:
    print("Divisible by 11 not 5.")

elif num%5==0 and num%11==0:
    print("Divisible by 5 and 11.")

elif num%5!=0 and num%11!=0:
    print("Neither divisible by 5 nor 11.")
else:
    print("Invalid input, Please try again.")