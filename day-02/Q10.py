'''Given a string of odd length greater than 7, return a new string made of the middle three
characters of a given String
Given:
str1 = "RakeshzipPetabb"
Output
zip
str2 = "JazzbonAyxx"
Output
Bon'''

new_str = str(input("Enter the string: "))

if len(new_str) > 7:
    midd = int((len(new_str) / 2)-1)
    endd = int(midd + 3)
    print(new_str[midd:endd])
else:
    print("Provide a long string.")