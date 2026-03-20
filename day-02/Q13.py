''' Given an input string with the combination of the lower and upper case arrange characters
in such a way that all lowercase letters should come first. '''

strr = str(input("Enter the string: "))

lst = []
lst2 = []

for letter in strr:
    if letter.islower():
        lst.append(letter)
    elif letter.isupper():
        lst2.append(letter)
    else:
        print("Invalid input")

lst3 = "".join(lst + lst2)
print(lst3)           