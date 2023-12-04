file = open("input.txt")

file_inp = file.readlines()
result = 0

# Parsing cleanup
file_inp = list(map(lambda x: x[10:].strip(), file_inp))
file_inp = list(map(lambda x: x.split(" | "), file_inp))

print(file_inp)

for stringList in file_inp:
    stringList[0] = stringList[0].replace("  ", " ")
    stringList[1] = stringList[1].replace("  ", " ")
    stringList[0] = stringList[0].split(" ")
    stringList[1] = stringList[1].split(" ")
    stringList[0] = set(map(lambda x: int(x), stringList[0]))
    stringList[1] = set(map(lambda x: int(x) if x else None, stringList[1]))

    result += int(pow(2, len(stringList[0].intersection(stringList[1]))-1))
    print(result)

print(result)
