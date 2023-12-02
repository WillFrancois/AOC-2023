import re

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

inp_file = open("input.txt")
lines = inp_file.readlines()
game_line = []
result = 0


def is_all_less_in_list(color_list, max_value):
    for i in color_list:
        if i <= max_value:
            continue
        else:
            return False
    return True


for i in lines:
    # Determine max of balls in games
    game_line = re.split("Game \d+: ", i)[1:][0]
    game_line = game_line.split(";")

    all_red = re.findall("\d+(?= red)", i)
    all_green = re.findall("\d+(?= green)", i)
    all_blue = re.findall("\d+(?= blue)", i)

    all_red = list(map(lambda x: int(x), all_red))
    all_green = list(map(lambda x: int(x), all_green))
    all_blue = list(map(lambda x: int(x), all_blue))

    if is_all_less_in_list(all_red, MAX_RED) and is_all_less_in_list(all_green, MAX_GREEN) and is_all_less_in_list(all_blue, MAX_BLUE):
        # Add to score if possible
        game_num = re.search("(?<=Game )\d+(?=:)", i)
        game_num = int(game_num[0])
        result += game_num

print(result)
