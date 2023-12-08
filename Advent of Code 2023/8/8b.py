'''
For example:

LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
Here, there are two starting nodes, 11A and 22A (because they both end with A). As you follow each left/right instruction, use that instruction to simultaneously navigate away from both nodes you're currently on. Repeat this process until all of the nodes you're currently on end with Z. (If only some of the nodes you're on end with Z, they act like any other node and you continue as normal.) In this example, you would proceed as follows:

Step 0: You are at 11A and 22A.
Step 1: You choose all of the left paths, leading you to 11B and 22B.
Step 2: You choose all of the right paths, leading you to 11Z and 22C.
Step 3: You choose all of the left paths, leading you to 11B and 22Z.
Step 4: You choose all of the right paths, leading you to 11Z and 22B.
Step 5: You choose all of the left paths, leading you to 11B and 22C.
Step 6: You choose all of the right paths, leading you to 11Z and 22Z.
So, in this example, you end up entirely on nodes that end in Z after 6 steps.

Simultaneously start on every node that ends with A. How many steps does it take before you're only on nodes that end with Z?
'''

from math import gcd

def lcm_of_list(numbers):
    lcm = numbers[0]
    for i in range(1, len(numbers)):
        lcm = lcm * numbers[i] // gcd(lcm, numbers[i])
    return lcm

file = open("input.txt", "r").read()
file = file.split("\n\n")
steps = file[0]
mappings = file[1]


cur_nodes = []
mappings = mappings.split("\n")
maps = {}
for mapping in mappings:
    mapping = mapping.split(" = ")
    node = mapping[0]
    if node[-1] == 'A':
        cur_nodes.append(node)
    directions = mapping[1].strip("(").strip(")").split(", ")
    maps[node] = (directions[0], directions[1])

total_steps = []
for node in cur_nodes:
    cur_step = 0
    cur_node = node
    while cur_node[-1] != 'Z':
        cur_directions = maps[cur_node]
        idx = 0 if cur_step == 0 else cur_step % (len(steps))
        instruction = steps[idx]
        next_node = ""
        if instruction == "L":
            next_node = cur_directions[0]
        else:
            next_node = cur_directions[1]
        cur_step += 1
        cur_node = next_node
    total_steps.append(cur_step)

print(lcm_of_list(total_steps))