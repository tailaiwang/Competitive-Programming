'''
Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
'''

file = open("input.txt", "r")
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0"
}
sum = 0
for line in file.readlines():
    line = line.strip("\n")
    first_dig = None
    last_dig = None
    found = []
    for digit in digits:
        if digit in line:
            found.append((line.find(digit), digit))
            found.append((line.rfind(digit), digit))
    for key in mapping:
        if key in line:
            found.append((line.find(key), mapping[key]))
            found.append((line.rfind(key), mapping[key]))
    found = sorted(found)
    print(found)
    sum += int(found[0][1] + found[-1][1])
    print(int(found[0][1] + found[-1][1]))
print(sum)
        
