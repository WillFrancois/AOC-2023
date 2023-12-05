seed_values = {}

file_inp = open("input.txt")
result = 9999999999

lines = file_inp.readlines()
lines = list(map(lambda x: x.strip() if x.strip() != '' else None, lines))
lines.append(None)

seeds = lines[0].split("seeds: ")
seeds = seeds[1:]
seeds = seeds[0].split(" ")
seeds = list(map(lambda x: int(x), seeds))
for i in seeds:
    seed_values[i] = i


def test_search_list(map_string, index):
    instructions = map_string.split(" ")
    instructions = list(map(lambda x: int(x), instructions))

    start = instructions[1]
    end = instructions[1] + instructions[2]
    value = instructions[0]

    if index >= start and index < end:
        return value + (index - start)
    else:
        return -1


for line_number in range(len(lines)):
    search_strings = ['seed-to-soil map:', 'soil-to-fertilizer map:',
                      'fertilizer-to-water map:', 'water-to-light map:',
                      'light-to-temperature map:',
                      'temperature-to-humidity map:',
                      'humidity-to-location map:'
                      ]

    if lines[line_number] in search_strings:
        matched = []
        new_map = lines[line_number+1:lines.index(
            None, line_number, len(lines))]

        for i in new_map:
            for j in seed_values.keys():
                if test_search_list(i, seed_values[j]) == -1:
                    pass
                elif j not in matched:
                    matched.append(j)
                    seed_values[j] = test_search_list(i, seed_values[j])
                    continue
                seed_values[j] = seed_values[j]

        matched.clear()

print(min(seed_values.values()))
