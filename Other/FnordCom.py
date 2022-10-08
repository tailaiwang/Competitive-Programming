# Coding Challenge: Passwords
# Nimble SWE Intern Interview (Winter 2023)
# Tailai Wang, University of Waterloo CS/BBA
# April 4th, 2022

# Using sys to read from file input
import sys


''' 
    To Run this Script
        1. python FnordCom.py < [INPUT FILE] > [OUTPUT FILE]
        2. use diff-checker to compare [OUTPUT FILE] with intended output
    Rules / Constraints
        1. Password must contain at least one vowel
        2. Password cannot contain three consecutive vowels or three consecutive consonants
        3. Password cannot contain two consecutive occurences of the same letter, except for 'ee' or 'oo'

    Considerations Made
        1. Decided Against making additional helper functions for each of the rules in order to maintain single-pass runtime.
            a) If I had to make the code more scalable (i.e. if need to add more rules in the future), I would separate the individual rules into helper functions
            b) As it stands, I think the single-pass loop is readable enough and I wouldn't sacrifice O(n) runtime for O(3n) runtime with marginal modularization improvements
        2. Decided against using regex to simplify the process
            a) Importing 're' and testing/validating the regex string doesn't seem wise from a hand-off perspective.
    
'''
# passValidator Helper Function
# Input: password (String)
# Output: boolean (True if acceptable, False if unacceptable)
# Runtime: Single Pass O(n) time complexity
# Space: O(1)
def passValidator(password):
    vowels = [ 'a', 'e', 'o', 'i', 'u']
    oneVowel = False
    consecutiveOccurences = 1
    consecutiveVowels = 0
    consecutiveConsonants = 0
    lastLetter = ''

    for char in password:
        # Check if we have consecutive occurences of same letter
        if lastLetter == '':
            lastLetter = char
        else:
            if char == lastLetter:
                consecutiveOccurences += 1
            else:
                consecutiveOccurences = 1
                lastLetter = char
            if consecutiveOccurences == 2 and lastLetter not in ['e','o']:
                return False

        # Check for consecutive consonants/vowels
        if char in vowels:
            oneVowel = True
            consecutiveConsonants = 0
            consecutiveVowels += 1
            if consecutiveVowels == 3:
                return False
        else:
            consecutiveVowels = 0
            consecutiveConsonants += 1
            if consecutiveConsonants == 3:
                return False
    
    # Since we return false if Rules 2/3 are violated, we just return if Rule 1 is Good
    return oneVowel


# Read line by line from file
for line in sys.stdin:
    line = line.strip()
    if line == "end":
        break
    if passValidator(line):
        print("<" + line + "> is acceptable.")
    else:
        print("<" + line + "> is not acceptable.")
            
