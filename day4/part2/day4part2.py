import functools

file = open("input.txt")

file_inp = file.readlines()
mult_list = [1] * len(file_inp)
result = 0

# Parsing cleanup
file_inp = list(map(lambda x: x[10:].strip(), file_inp))
file_inp = list(map(lambda x: x.split(" | "), file_inp))

print(file_inp)

for stringList in range(len(file_inp)):
    file_inp[stringList][0] = file_inp[stringList][0].replace("  ", " ")
    file_inp[stringList][1] = file_inp[stringList][1].replace("  ", " ")
    file_inp[stringList][0] = file_inp[stringList][0].split(" ")
    file_inp[stringList][1] = file_inp[stringList][1].split(" ")
    file_inp[stringList][0] = set(
        map(lambda x: int(x), file_inp[stringList][0]))
    file_inp[stringList][1] = set(
        map(lambda x: int(x) if x else None, file_inp[stringList][1]))

    for i in range(len(file_inp[stringList][0].intersection(file_inp[stringList][1]))):
        mult_list[stringList + i + 1] += mult_list[stringList]

print(functools.reduce(lambda x, y: x + y, mult_list))
