import re

file = open("input.txt")
lines = file.readlines()
path_dict = {}
current_area = "AAA"
result = 0

for line in lines:
    all_parts = re.findall(r"\w{3,3}", line)
    if len(all_parts) == 3:
        path_dict[all_parts[0]] = [all_parts[1], all_parts[2]]

while current_area != "ZZZ":
    for char in lines[0].strip():
        result += 1
        if char == "L":
            current_area = path_dict[current_area][0]
        elif char == "R":
            current_area = path_dict[current_area][1]

print(result)
