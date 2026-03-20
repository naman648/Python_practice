'''3. two strings, s1, and s2 return a new string made of the first, middle, and last characters each
input string
Given:
s1 = "America"
s2 = "Japan"
Expected Output:
AJrpan 
'''
str1 = str(input("Enter the first string: "))
str2 = str(input("Enter the second string: "))

first_char = str1[:1] + str2[:1]
mid = int(len(str1) / 2)
str5 = str1[mid]
str6 = str2[2:]
result = first_char + str5 + str6
print(result)
