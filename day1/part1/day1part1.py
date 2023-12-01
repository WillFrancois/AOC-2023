file_inp = open("input.txt")
line_list = file_inp.readlines()
result = 0

for i in range(len(line_list)):
    left_int = None
    right_int = None
    word = line_list[i]
    for j in word:
        if j in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if left_int is None:
                left_int = j
            right_int = j

    result += int(left_int + right_int)

print(result)
