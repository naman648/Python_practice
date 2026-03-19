''' 1. A student will not be allowed to sit in exam if his/her attendence is less than 75%. Take following input from user 
Number of classes held, Number of classes attended, And print percentage of class attended 
Is student is allowed to sit in exam or not. '''

print("---ATTENDANCE CALCULATION AND ELIGIBILITY FOR EXAM---")

held = int(input("Enter the no. of classes held: "))
attd = int(input("Enter the no. of classes attended: "))

percent = attd/held * 100
print(f"Attendance percent: {percent}%")

if percent > 75:
    print("Eligibility: Eligible for exam")
else:
    print("Eligibility: Not Eligible for exam")



