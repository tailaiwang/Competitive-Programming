'''
Now, the above example goes very differently:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
32T3K is still the only one pair; it doesn't contain any jokers, so its strength doesn't increase.
KK677 is now the only two pair, making it the second-weakest hand.
T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.
With the new joker rule, the total winnings in this example are 5905.

'''


from collections import Counter
file = open("input.txt", "r")
cards_mapping  = {
    'A': 'E',
    'K': 'D',
    'Q': 'C',
    'J': '1',
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
    price = int(line[1])
    joker_count = 0
    for i in range(len(hand)):
        if hand[i] == 'J':
            joker_count += 1
        hand[i] = cards_mapping[hand[i]]
    counter = Counter(hand)
    lst = list(counter.items())
    organized = sorted(lst, key = lambda t: (t[1], t[0]), reverse=True)
    first = organized[0][0]
    num_highest = organized[0][1] if first != '1' else 1
    num_second_highest = 0
    if len(organized) > 1:
        num_second_highest = organized[1][1]
    num_highest += joker_count
    if num_highest == 1:
        ones.append((hand, price))
    elif num_highest == 2:
        if num_second_highest == 2:
            twos_pairs.append((hand, price))
        else:
            pairs.append((hand, price))
    elif num_highest == 3:
        if num_second_highest == 2:
            fulls.append((hand, price))
        else:
            threes.append((hand, price))
    elif num_highest == 4:
        fours.append((hand, price))
    else:
        fives.append((hand, price))
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