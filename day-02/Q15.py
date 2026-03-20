''' Find all occurrences of “USA” from right to left in a given string ignoring the case. also
display the position
Given:
str1 = "Welcome to USA. usa awesome, isn't it? '''

str1 = input("Enter the string: ")

s = str1.lower()   # ignore case
count = 0

print("Positions (from right to left):")

# traverse from right to left
for i in range(len(s) - 1, -1, -1):
    if s[i:i+3] == "usa":
        print(i)
        count += 1

print("Total occurrences:", count)
