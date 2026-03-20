'''Accept 20 numbers from user and display sum of only even numbers.'''

e_lst = []
for i in range(1,21):
    num = int(input("Enter the number: "))
    if num%2 == 0:
        e_lst.append(num)
total_sum = sum(e_lst)
print("Total sum of only EVENS: " , total_sum)