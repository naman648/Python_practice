'''Accept 10 integers from user and print their average value on the screen'''

print("----AVERAGE OF 10 VALUES----")

lst = []

for i in range(1,11):
    num = int(input("Enter the number: "))
    lst.append(num)

total_sum = sum(lst)
avg = total_sum / 10
print("Average: ", avg)
