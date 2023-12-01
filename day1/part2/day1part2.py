nums_as_words = ["one", "two", "three", "four",
                 "five", "six", "seven", "eight", "nine", "zero"]

nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

result = 0

file_inp = open("input.txt")
lines = file_inp.readlines()

for line in lines:
    left_num = None
    right_num = None
    # Reassign line to remove \n character
    line = line[:len(line)-1]

    for j in range(len(line)):
        test_line = line[j:]
        # Word check
        for k in nums_as_words:
            if k == test_line[:len(k)]:
                if left_num is None:
                    left_num = nums[nums_as_words.index(k)]
                right_num = nums[nums_as_words.index(k)]
        # Num check
        for k in nums:
            if k == test_line[0]:
                if left_num is None:
                    left_num = k
                right_num = k

    result += int(left_num + right_num)

print(result)
