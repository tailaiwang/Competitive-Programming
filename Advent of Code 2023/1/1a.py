'''
For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

'''

file = open("input.txt", "r")
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
sum = 0
for line in file.readlines():
    line = line.strip("\n")
    first_dig = None
    last_dig = None
    for char in line:
        if char in digits:
            if first_dig is None:
                first_dig = char
            else:
                last_dig = char

    if last_dig is None:
        sum += int(first_dig + first_dig)
    else:
        sum += int(first_dig + last_dig)
print(sum)
        
