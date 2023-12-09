file = open("input.txt")
games = file.readlines()
games = list(map(lambda x: x.strip(), games))
result = 0

hands = list(map(lambda x: list(x.split(" ")[0]), games))
bets = list(map(lambda x: int(x.split(" ")[1]), games))

let_to_num = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

# Change letters to numbers
for i in hands:
    for j in range(len(i)):
        if i[j] in let_to_num.keys():
            i[j] = let_to_num[i[j]]
        else:
            i[j] = int(i[j])

bet_value_index = 0
for i in range(len(hands)):
    hands[i] = (bet_value_index, hands[i])
    bet_value_index += 1


hand_rank_list = [[], [], [], [], [], [], []]

# Check hands for attributes
for i in hands:
    attr_dict = {}
    for j in i[1]:
        if j not in attr_dict.keys():
            attr_dict[j] = i[1].count(j)
    if 5 in attr_dict.values():
        hand_rank_list[6].append(i)
    elif 4 in attr_dict.values():
        hand_rank_list[5].append(i)
    elif 3 in attr_dict.values() and 2 in attr_dict.values():
        hand_rank_list[4].append(i)
    elif 3 in attr_dict.values():
        hand_rank_list[3].append(i)
    elif list(attr_dict.values()).count(2) == 2:
        hand_rank_list[2].append(i)
    elif 2 in attr_dict.values():
        hand_rank_list[1].append(i)
    elif 1 in attr_dict.values():
        hand_rank_list[0].append(i)


for power_level in hand_rank_list:
    power_level.sort(lambda x: x[1])


current_rank = 1
for i in range(len(hand_rank_list)):
    for j in hand_rank_list[i]:
        result += bets[j[0]] * current_rank
        current_rank += 1

print(result)
