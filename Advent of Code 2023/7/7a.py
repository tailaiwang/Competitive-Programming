'''
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
This example shows five hands; each hand is followed by its bid amount. Each hand wins an amount equal to its bid multiplied by its rank, where the weakest hand gets rank 1, the second-weakest hand gets rank 2, and so on up to the strongest hand. Because there are five hands in this example, the strongest hand will have rank 5 and its bid will be multiplied by 5.

So, the first step is to put the hands in order of strength:

32T3K is the only one pair and the other hands are all a stronger type, so it gets rank 1.
KK677 and KTJJT are both two pair. Their first cards both have the same label, but the second card of KK677 is stronger (K vs T), so KTJJT gets rank 2 and KK677 gets rank 3.
T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card, so it gets rank 5 and T55J5 gets rank 4.
Now, you can determine the total winnings of this set of hands by adding up the result of multiplying each hand's bid with its rank (765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5). So the total winnings in this example are 6440.
'''

from collections import Counter
file = open("input.txt", "r")
cards_mapping  = {
    'A': 'E',
    'K': 'D',
    'Q': 'C',
    'J': 'B',
    'T': 'A',
    '9': '9',
    '8': '8',
    '7': '7',
    '6': '6',
    '5': '5',
    '4': '4',
    '3': '3',
    '2': '2'
}
fives = []
fours = []
fulls = []
threes = []
twos_pairs = []
pairs =[]
ones = []

for line in file.readlines():
    line  = line.strip("\n").split(" ")
    hand = list(line[0])
    rank = int(line[1])
    for i in range(len(hand)):
        hand[i] = cards_mapping[hand[i]]
    counter = Counter(hand)
    lst = list(counter.items())
    organized = sorted(lst, key = lambda t: (t[1], t[0]), reverse=True)
    if organized[0][1] == 5:
        fives.append((hand, rank))
    elif organized[0][1] == 4:
        fours.append((hand, rank))
    elif organized[0][1] == 3:
        if organized[1][1] == 2:
            fulls.append((hand, rank))
        else:
            threes.append((hand, rank))
    elif organized[0][1] == 2:
        if organized[1][1] == 2:
            twos_pairs.append((hand, rank))
        else:
            pairs.append((hand, rank))
    else:
        ones.append((hand, rank))
    
fives = sorted(fives, key = lambda t: t[0])
fours = sorted(fours, key = lambda t: t[0])
fulls = sorted(fulls, key = lambda t: t[0])
threes = sorted(threes, key = lambda t: t[0])
twos_pairs = sorted(twos_pairs, key = lambda t: t[0])
pairs = sorted(pairs, key = lambda t: t[0])
ones = sorted(ones, key = lambda t: t[0])

rank = 1
sum = 0
for hand in ones:
    sum += hand[1] * rank
    rank += 1

for hand in pairs:
    sum += hand[1] * rank
    rank += 1

for hand in twos_pairs:
    sum += hand[1] * rank
    rank += 1

for hand in threes:
    sum += hand[1] * rank
    rank += 1

for hand in fulls:
    sum += hand[1] * rank
    rank += 1

for hand in fours:
    sum += hand[1] * rank
    rank += 1

for hand in fives:
    sum += hand[1] * rank
    rank += 1

print(sum)