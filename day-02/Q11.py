'''Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1
Given:
s1 = "Ault"
s2 = "Kelly"
Expected Output:
AuKellylt '''

str1 = str(input("Enter first string: "))
str2 = str(input("Enter second string: "))

str3 = str1[:2]
str4 = str1[-2:len(str1)]

concat_str = str3 + str2 + str4
print(concat_str)