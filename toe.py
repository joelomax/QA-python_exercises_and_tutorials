"""
TOE: Write a program that will find all such numbers which are divisible by 7, but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be returned in a comma-separated sequence on a single line.
This must be on your GitHub by 9am tomorrow morning, and 2 random people will be chosen to pull their GitHub up and talk through their solution.
"""
max = 3200
for i in range (2000, max):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end =",")