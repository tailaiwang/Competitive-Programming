'''
Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and the second value is the length of the range. So, in the first line of the example above:

seeds: 79 14 55 13
This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is 46.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest location number that corresponds to any of the initial seed numbers?

'''

file = open("input.txt", "r").read()

maps = file.split("\n\n")

seeds = maps[0].split(": ")[1].split(" ")
seeds = [int(i) for i in seeds]
current_ranges = []
for i in range(0, len(seeds), 2):
    start = seeds[i]
    length = seeds[i + 1]
    current_ranges.append((start, start + length - 1))

# skip 0 because we just extracted the seeds from it
next_ranges = []
added = []
for i in range(1, len(maps)):
    map = maps[i].split(":\n")
    title = map[0]
    print("Now investigating " + title)
    ranges  = map[1].split("\n")
    for r in ranges:
        r = r.split(" ")
        destination = int(r[0])
        source  = int(r[1])
        length = int(r[2])
        for item in current_ranges:
            source_x = max(item[0], source)
            source_y = min(item[1], source + length - 1)
            if source_x < source_y:
                added.append((source_x, source_y))
                dest_x = destination + (source_x - source)
                dest_y = destination + (source_y - source)
                next_ranges.append((dest_x, dest_y))
               # print("Took " + str((item[0], item[1])) + " and converted to range " + str((source_x, source_y)) + " and dest " + str((dest_x, dest_y)))
    added = sorted(added)
   # print("added pre " + str(added))
    merged = []
    for next in added:
        if not merged or next[0] > merged[-1][1] + 1:
            merged.append(next)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], next[1]))
    added = merged
   # print("added post " + str(added))
    for remaining in current_ranges:
        flag = False
        for add in added:
            possible_x = max(remaining[0], add[0])
            possible_y = min(remaining[1], add[1])
            overlap = True if possible_x < possible_y else False
            if overlap:
                if remaining[0] < possible_x:
                    if (remaining[0], possible_x - 1) not in added:
                        next_ranges.append((remaining[0], possible_x - 1))
                        #print("Left Took " + str((remaining[0], remaining[1])) + " and clashed with added " + str((add[0], add[1])) + " for remain " + str((remaining[0], possible_x - 1)))
                if remaining[1] > possible_y:
                    if (possible_y + 1, remaining[1]) not in added:
                        next_ranges.append((possible_y + 1, remaining[1]))
                        # print("Right Took " + str((remaining[0], remaining[1])) + " and clashed with added " + str((add[0], add[1])) + " for remain " + str((possible_y + 1, remaining[1])))
                flag = True
            
        if not flag:
            next_ranges.append((remaining[0], remaining[1]))
    current_ranges = next_ranges
    # print(sorted(current_ranges))
    next_ranges = []
    added = []
print(min(current_ranges))
