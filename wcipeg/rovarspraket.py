#rovarspraket

word = input()

consonant =     "bcdfghjklmnpqrstvwxyz"
closestVowel =  "aaeeeiiiiooooouuuuuuu"
nextConsonant = "cdfghjklmnpqrstvwxyzz"

newWord = ""
for i in range(len(word)):
    j = consonant.find (word[i])
    newWord = newWord + word[i]  # the orginal letter is always copied over
    if j > -1:                   # if it's not a vowel add the closest vowel and
                                 # next consonant   
        newWord = newWord + closestVowel [j] + nextConsonant[j]

print (newWord)
