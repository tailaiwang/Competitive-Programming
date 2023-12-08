'''
This format defines each node of the network individually. For example:

RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
Starting with AAA, you need to look up the next element based on the next left/right instruction in your input. In this example, start with AAA and go right (R) by choosing the right element of AAA, CCC. Then, L means to choose the left element of CCC, ZZZ. By following the left/right instructions, you reach ZZZ in 2 steps.

Of course, you might not find ZZZ right away. If you run out of left/right instructions, repeat the whole sequence of instructions as necessary: RL really means RLRLRLRLRLRLRLRL... and so on. For example, here is a situation that takes 6 steps to reach ZZZ:

LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
Starting at AAA, follow the left/right instructions. How many steps are required to reach ZZZ?
'''

file = open("input.txt", "r").read()
file = file.split("\n\n")
steps = file[0]
mappings = file[1]

mappings = mappings.split("\n")
maps = {}
for mapping in mappings:
    mapping = mapping.split(" = ")
    node = mapping[0]
    directions = mapping[1].strip("(").strip(")").split(", ")
    maps[node] = (directions[0], directions[1])

step = 0
cur_node = 'AAA'

while cur_node != 'ZZZ':
    cur_directions = maps[cur_node]
    idx = 0 if step == 0 else step % (len(steps))
    instruction = steps[idx]
    next_node = ""
    if instruction == "L":
        next_node = cur_directions[0]
    else:
        next_node = cur_directions[1]
    step += 1
    cur_node = next_node

print(step)
        