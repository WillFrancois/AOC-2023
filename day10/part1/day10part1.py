import sys
sys.setrecursionlimit(9999)

file = open("test_input.txt")
lines = file.readlines()
lines = list(map(lambda x: x.strip(), lines))

location_map = {}
distance_map = {}
starting_location = ()
farthest_location = ()

for y in range(len(lines)):
    for x in range(len(lines[y])):
        location_map[(y, x)] = []
        match lines[y][x]:
            case "|":
                location_map[(y, x)].append((y-1, x))
                location_map[(y, x)].append((y+1, x))
            case "-":
                location_map[(y, x)].append((y, x-1))
                location_map[(y, x)].append((y, x+1))
            case "7":
                location_map[(y, x)].append((y, x-1))
                location_map[(y, x)].append((y+1, x))
            case "F":
                location_map[(y, x)].append((y, x+1))
                location_map[(y, x)].append((y+1, x))
            case "L":
                location_map[(y, x)].append((y, x+1))
                location_map[(y, x)].append((y-1, x))
            case "J":
                location_map[(y, x)].append((y, x-1))
                location_map[(y, x)].append((y-1, x))
            case "S":
                starting_location = (y, x)

for key in list(location_map.keys()):
    if starting_location in location_map[key]:
        location_map[starting_location].append(key)

cull_list = []
for key in location_map:
    if location_map[key] == []:
        cull_list.append(key)

for element in cull_list:
    location_map.pop(element)
del cull_list

# print(location_map)

# for key in range(len(location_map.keys())):
#     location_ranges = range(len(location_map[list(location_map.keys())[key]]))
#     for i in location_ranges:
#         if location_map[list(location_map.keys())[key]][i] in list(distance_map.keys()):
#             continue
#         distance_map[location_map[list(location_map.keys())[key]][i]] = key + 1
#
# print(distance_map)


def dfs(starting_node, steps):
    try:
        if distance_map[starting_node] > steps:
            distance_map[starting_node] = steps
        else:
            return
    except KeyError:
        pass
    distance_map[starting_node] = steps
    for i in location_map[starting_node]:
        dfs(i, steps + 1)


dfs(starting_location, 0)

print(max(list(distance_map.values())))
