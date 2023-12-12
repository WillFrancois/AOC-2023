file = open("test_input.txt")
lines = file.readlines()
result = 0

# Get spring mappings
spring_map = list(map(lambda x: list(x.split(" "))[1], lines))
spring_map = list(map(lambda x: x.strip(), spring_map))
spring_map = list(map(lambda x: x.split(","), spring_map))
for mapping in range(len(spring_map)):
    spring_map[mapping] = list(map(lambda x: int(x), spring_map[mapping]))


# Get spring areas
spring_areas = list(map(lambda x: list(x.split(" "))[0], lines))
spring_areas = list(map(lambda x: x.strip(), spring_areas))


def is_area_to_map(spring_map_list, spring_area_element):
    current_length_run = 0
    length_run_list = []

    for i in range(len(spring_area_element)):
        if spring_area_element[i:][0] == "#":
            current_length_run += 1
        elif spring_area_element[i:][0] != "#" and current_length_run > 0:
            length_run_list.append(current_length_run)
            current_length_run = 0

    if current_length_run > 0:
        length_run_list.append(current_length_run)

    if length_run_list == spring_map_list:
        return True

    return False


def generate_spring_area(spring_area_element, permutation_list=[]):
    spring_area_element = str(spring_area_element)
    if "?" in spring_area_element:
        q_index = spring_area_element.find("?")
        if q_index > -1:
            element_list = list(spring_area_element)
            element_list[q_index] = "."
            generate_spring_area(''.join(element_list))
            element_list[q_index] = "#"
            generate_spring_area(''.join(element_list))
    else:
        if spring_area_element not in permutation_list:
            permutation_list.append(spring_area_element)
    return permutation_list


for line_number in range(len(lines)):
    print(lines[line_number])
    working_spring_area = generate_spring_area(
        spring_areas[line_number])
    for area in working_spring_area:
        if is_area_to_map(spring_map[line_number], area):
            result += 1
    working_spring_area.clear()

print(result)
