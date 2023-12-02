import re

inp_file = open("input.txt")
lines = inp_file.readlines()
game_line = []
result = 0


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

    red_max = max(all_red)
    green_max = max(all_green)
    blue_max = max(all_blue)

    result += red_max * green_max * blue_max

print(result)
