import re
import math

file = open("input.txt")
lines = file.readlines()
path_dict = {}
current_area = []
cur_res = []
result = 1

for line in lines:
    all_parts = re.findall(r"\w{3,3}", line)
    if len(all_parts) == 3:
        if all_parts[0][2] == 'A':
            current_area.append(all_parts[0])
        path_dict[all_parts[0]] = [all_parts[1], all_parts[2]]

for area in range(len(current_area)):
    res_hold = 0
    while current_area[area][2] != "Z":
        for char in lines[0].strip():
            res_hold += 1
            if char == "L":
                print(current_area)
                current_area[area] = path_dict[current_area[area]][0]
            elif char == "R":
                current_area[area] = path_dict[current_area[area]][1]
    cur_res.append(res_hold)

print(math.lcm(*cur_res))
