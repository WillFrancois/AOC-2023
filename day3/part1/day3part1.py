import re

file_inp = open("input.txt")
contents = file_inp.readlines()
result = 0


def clamp_vals(n, max_length):
    if n < 0:
        return 0
    elif n > max_length:
        return max_length
    else:
        return n


def find_numbers_locations(file_contents):
    number_locations = []

    for i in range(len(file_contents)):
        number_results = re.finditer(r"(?<=.)?\d+(?=.)?", file_contents[i])
        while True:
            try:
                locations = [i]
                locations.append(list(number_results.__next__().span()))
                number_locations.append(locations)
            except StopIteration:
                break

    return number_locations


def find_special_characters(file_contents):
    special_character_locations = []

    for i in range(len(file_contents)):
        character_results = re.finditer(
            r"[^A-z0-9\.\\]", file_contents[i].strip())
        while True:
            try:
                location = (i, character_results.__next__().span()[1]-1)
                special_character_locations.append(location)
            except StopIteration:
                break

    return special_character_locations


number_locations = find_numbers_locations(contents)
special_character_locations = find_special_characters(contents)


def is_schematic(word_range, list_of_special_character_locations):
    global result

    y_bounds = [clamp_vals(word_range[0] - 1, len(contents)),
                clamp_vals(word_range[0] + 2, len(contents))]
    x_bounds = [clamp_vals(word_range[1][0] - 1, len(contents[0])),
                clamp_vals(word_range[1][1] + 1, len(contents[0]))]

    for i in range(y_bounds[0], y_bounds[1]):
        for j in range(x_bounds[0], x_bounds[1]):
            if (i, j) in list_of_special_character_locations:
                result += int(contents[word_range[0]
                                       ][word_range[1][0]:word_range[1][1]])
                return True

    return False


for i in number_locations:
    is_schematic(i, special_character_locations)

print(result)
