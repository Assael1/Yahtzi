import random

# functios for points


def one(dice):
    count = 0
    for i in dice:
        if i[0] == 1:
            count += 1
    return count


def two(dice):
    count = 0
    for i in dice:
        if i[0] == 2:
            count += 1
    return count*2


def three(dice):
    count = 0
    for i in dice:
        if i[0] == 3:
            count += 1
    return count*3


def four(dice):
    count = 0
    for i in dice:
        if i[0] == 4:
            count += 1
    return count*4


def five(dice):
    count = 0
    for i in dice:
        if i[0] == 5:
            count += 1
    return count*5


def six(dice):
    count = 0
    for i in dice:
        if i[0] == 6:
            count += 1
    return count*6


def X3(dice):
    dice0 = list(dice)
    dice0.sort()
    if dice0[0][0] == dice0[1][0] == dice0[2][0] or dice0[2][0] == dice0[3][0] == dice0[4][0] or dice0[1][0] == dice0[2][0] == dice0[3][0]:
        return sum(row[0] for row in dice)
    return 0


def X4(dice):
    dice0 = list(dice)
    dice0.sort()
    if dice0[0][0] == dice0[1][0] == dice0[2][0] == dice0[3][0] or dice0[1][0] == dice0[2][0] == dice0[3][0] == dice0[4][0]:
        return sum(row[0] for row in dice)
    return 0


def full_house(dice):
    dice0 = list(dice)
    dice0.sort()
    if dice0[0][0] == dice0[1][0] == dice0[2][0] and dice0[2][0] != dice0[3][0] == dice0[4][0]:
        return 25
    if dice0[0][0] == dice0[1][0] != dice0[2][0] and dice0[2][0] == dice0[3][0] == dice0[4][0]:
        return 25
    return 0


def small(dice):
    dice0 = list(dice)
    dice0.sort()
    if dice0[4][0] == dice0[3][0]+1 == dice0[2][0]+2 == dice0[1][0]+3 or dice0[3][0] == dice0[2][0]+1 == dice0[1][0]+2 == dice0[0][0]+3:
        return 30
    if dice0[3][0] == dice0[2][0]:
        if dice0[4][0] == dice0[2][0]+1 == dice0[1][0]+2 == dice0[0][0]+3:
            return 30
    if dice0[2][0] == dice0[1][0]:
        if dice0[4][0] == dice0[3][0]+1 == dice0[1][0]+2 == dice0[0][0]+3:
            return 30
    return 0


def long(dice):
    dice0 = list(dice)
    dice0.sort()
    if dice0[4][0] == dice0[3][0]+1 == dice0[2][0]+2 == dice0[1][0]+3 == dice0[0][0]+4:
        return 40
    return 0


def yatzy(dice):
    if dice[0][0] == dice[1][0] == dice[2][0] == dice[3][0] == dice[4][0]:
        return 50
    return 0


def check_for_bonus(score):
    if sum(score[0:6]) > 63:
        score[13] = 35
    return score


def show_points(score, temp, points, dice):
    for i in range(len(score)):
        if score[i] != 0:
            temp[i] = score[i]
        if score[i] == 0:
            temp[i] = "[" + str(points[i]) + "]"
    return temp


def bonus(score, options_player, options):
    counter = 0
    for i in range(6):
        if options[i] is not options_player:
            counter += -3*(i+1)+score[i]
    return counter


def change_dice(dice, turn, window, tries):
    if dice[0][1] == False:
        dice[0][0] = random.randint(1, 6)
    else:
        dice[0][1] = True
    if dice[1][1] == False:
        dice[1][0] = random.randint(1, 6)
    else:
        dice[1][1] = True
    if dice[2][1] == False:
        dice[2][0] = random.randint(1, 6)
    else:
        dice[2][1] = True
    if dice[3][1] == False:
        dice[3][0] = random.randint(1, 6)
    else:
        dice[3][1] = True
    if dice[4][1] == False:
        dice[4][0] = random.randint(1, 6)
    else:
        dice[4][1] = True
    return dice
