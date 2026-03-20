'''Ask user number of terms to be generated of a series. Generate numbers for the following series and find its addition
[9 + 99 + 999 + 9999+……..] (G.P.)'''

import math
n = int(input("Enter the number of terms: "))
term = 0
total = 0

for i in range(n):
    term = term*10 + 9
    print(term, end = " + ")
    total = total + term

print("\n GP's Total sum: ", total)

    
