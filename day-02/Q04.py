'''Take integer inputs from user until he/she presses q ( Ask to press q to quit after every
integer input ). Print average and product of all numbers.'''

num = 2
e_lst = []
while(num>1):
    nums = input("Enter the number: ")
    if nums == 'q':
        break
    e_lst.append(nums)

'''Here we had a string list which we wanted to convert into a int list so came up with this
solution: new_list_name = [int(nums) for nums in <string_list_name>]'''

new_lst = [int(nums) for nums in e_lst]
length = len(new_lst)
sum_of_all = sum(new_lst)
avg = sum_of_all / length

print ("Average: ", avg)
prod = 1
for nums in new_lst:
    prod = prod * nums
print("Product: ", prod)