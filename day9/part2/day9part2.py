file = open("test_input.txt")
lines = file.readlines()
lines = list(map(lambda x: x.strip(), lines))
lines = list(map(lambda x: x.split(" "), lines))
result = 0

for line in range(len(lines)):
    lines[line] = list(map(lambda x: int(x), lines[line]))


def rec_list_call(input_list: list):
    if len(list(dict.fromkeys(input_list))) == 1:
        return input_list[0]

    new_list = []
    for i in range(1, len(input_list)):
        new_list.append(input_list[i] - input_list[i-1])

    return input_list[len(input_list) - 1] + rec_list_call(new_list)


for line in lines:
    line.reverse()
    result += rec_list_call(line)

print(result)
