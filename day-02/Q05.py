''' Given a number count the total number of digits in a number and also find sum of digits of
the number. '''

num = input("Enter the number: ")
count = len(num)
print("Count of number:", count)
new_lst = [int(nums) for nums in num]
sum_of_all = sum(new_lst)
print("Sum: ", sum_of_all)