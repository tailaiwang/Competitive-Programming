# Optimally solve the "9-card flipping game"
# Rules: 
# From a standard deck of 52 cards, lay 9 face up in a grid pattern.
# The objective is to empty the rest of the deck by flipping cards onto cards on the grid.
# Before flipping a card over, you must declare if it will be higher or lower than the card you're flipping it onto. 
# If the prediction is stricly correct (> or <), the flipped card replaces the bottom card as the top of the pile.
# If not, that specific pile will be eliminated from play

import random


# Perform a Monte Carlo Simulation of 100000 games

num_wins = 0
sample_size = 100000
for i in range(sample_size):
	# Remaining cards in the deck
	deck = []
	for i in range(2,15):
		for j in range(4):
			deck.append(i)

	# Cards currently in the grid
	hand = random.sample(deck, 9)
	for card in hand:
		deck.remove(card)

	while True:
		remaining_avg = sum(deck) / len(deck)
		furthest_dist_from_avg = 0
		furthest_card_from_avg = 0

		# loop to find card with furthest distance from remaining avg
		for i in range(len(hand)):
			cur_card = hand[i]
			cur_dist_from_avg = abs(remaining_avg - cur_card)
			if cur_dist_from_avg > furthest_dist_from_avg:
				furthest_dist_from_avg = cur_dist_from_avg
				furthest_card_from_avg = i
		
		# make draw and simulate decision
		furthest_card = hand[furthest_card_from_avg]
		flip = random.sample(deck, 1)[0]
		deck.remove(flip)
		if furthest_card > remaining_avg:
			# called lower
			if flip >= furthest_card:
				hand.remove(furthest_card)
			else:
				hand[furthest_card_from_avg] = flip
		else:
			# called higher
			if flip <= furthest_card:
				hand.remove(furthest_card)
			else:
				hand[furthest_card_from_avg] = flip

		# check win condition
		if len(deck) == 0:
			# we won
			num_wins += 1
			break
		elif len(hand) == 0:
			# we lost
			break
# Roughly 12 to 13% win rate
print("The Machine won " + str(num_wins) + " out of " + str(sample_size))