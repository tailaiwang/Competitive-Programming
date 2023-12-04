'''
This time, the above example goes differently:

Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
Card 1 has four matching numbers, so you win one copy each of the next four cards: cards 2, 3, 4, and 5.
Your original card 2 has two matching numbers, so you win one copy each of cards 3 and 4.
Your copy of card 2 also wins one copy each of cards 3 and 4.
Your four instances of card 3 (one original and three copies) have two matching numbers, so you win four copies each of cards 4 and 5.
Your eight instances of card 4 (one original and seven copies) have one matching number, so you win eight copies of card 5.
Your fourteen instances of card 5 (one original and thirteen copies) have no matching numbers and win no more cards.
Your one instance of card 6 (one original) has no matching numbers and wins no more cards.
Once all of the originals and copies have been processed, you end up with 1 instance of card 1, 2 instances of card 2, 4 instances of card 3, 8 instances of card 4, 14 instances of card 5, and 1 instance of card 6. In total, this example pile of scratchcards causes you to ultimately have 30 scratchcards!
'''

file = open("input.txt", "r")
multipliers = {}

sum = 0
card = 1
for line in file.readlines():
    if card not in multipliers:
        multipliers[card] = 1
    line = line.strip("\n")
    line = line.split(": ")
    data = line[1].split("| ")
    winners = data[0].split(" ")
    yours = data[1].split(" ")
    winners = [x for x in winners if x != '']
    yours = [x for x in yours if x != '']
    score = 0
    for number in yours:
        if number in winners:
            score += 1
    print(score)
    if score > 0:
        for i in range(card, card + score):
            if i + 1 not in multipliers:
                multipliers[i + 1] = 1+ multipliers[card]
            else:
                multipliers[i + 1] += multipliers[card]
    card += 1

for key in multipliers:
    sum += multipliers[key]

print(sum)