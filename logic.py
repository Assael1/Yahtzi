
from ui import *

options = ["1", "2", "3", "4", "5", "6", "x3", "x4",
           "full house", "small", "big", "yatzy", "sum", "second yatzy"]

# functions to give points after choose


def ok_choose(turn, score_player1, score_player2, dice_player1, dice_player2, options_player1, options_player2, place1, place2):
    if turn == 0:
        if place1 == "1":
            score_player1[0] = one(dice_player1)
            options_player1.remove("1")
        if place1 == "2":
            score_player1[1] = two(dice_player1)
            options_player1.remove("2")
        if place1 == "3":
            score_player1[2] = three(dice_player1)
            options_player1.remove("3")
        if place1 == "4":
            score_player1[3] = four(dice_player1)
            options_player1.remove("4")
        if place1 == "5":
            score_player1[4] = five(dice_player1)
            options_player1.remove("5")
        if place1 == "6":
            score_player1[5] = six(dice_player1)
            options_player1.remove("6")
        if place1 == "x3":
            score_player1[6] = X3(dice_player1)
            options_player1.remove("x3")
        if place1 == "x4":
            score_player1[7] = X4(dice_player1)
            options_player1.remove("x4")
        if place1 == "full house":
            score_player1[8] = full_house(dice_player1)
            options_player1.remove("full house")
        if place1 == "small":
            score_player1[9] = small(dice_player1)
            options_player1.remove("small")
        if place1 == "big":
            score_player1[10] = long(dice_player1)
            options_player1.remove("big")
        if place1 == "yatzy":
            score_player1[11] = yatzy(dice_player1)
            options_player1.remove("yatzy")
        if place1 == "sum":
            score_player1[12] = sum(row[0] for row in dice_player1)
            options_player1.remove("sum")
        if place1 == "second yatzy":
            if score_player1[11] != 0:
                score_player1[14] = yatzy(dice_player1)
            options_player1.remove("second yatzy")
    else:
        if place2 == "1":
            score_player2[0] = one(dice_player2)
            options_player2.remove("1")
        if place2 == "2":
            score_player2[1] = two(dice_player2)
            options_player2.remove("2")
        if place2 == "3":
            score_player2[2] = three(dice_player2)
            options_player2.remove("3")
        if place2 == "4":
            score_player2[3] = four(dice_player2)
            options_player2.remove("4")
        if place2 == "5":
            score_player2[4] = five(dice_player2)
            options_player2.remove("5")
        if place2 == "6":
            score_player2[5] = six(dice_player2)
            options_player2.remove("6")
        if place2 == "x3":
            score_player2[6] = X3(dice_player2)
            options_player2.remove("x3")
        if place2 == "x4":
            score_player2[7] = X4(dice_player2)
            options_player2.remove("x4")
        if place2 == "full house":
            score_player2[8] = full_house(dice_player2)
            options_player2.remove("full house")
        if place2 == "small":
            score_player2[9] = small(dice_player2)
            options_player2.remove("small")
        if place2 == "big":
            score_player2[10] = long(dice_player2)
            options_player2.remove("big")
        if place2 == "yatzy":
            score_player2[11] = yatzy(dice_player2)
            options_player2.remove("yatzy")
        if place2 == "sum":
            score_player2[12] = sum(row[0] for row in dice_player2)
            options_player2.remove("sum")
        if place2 == "second yatzy":
            if score_player2[11] != 0:
                score_player2[14] = yatzy(dice_player2)
            options_player2.remove("second yatzy")
    return options_player1, options_player2, score_player1, score_player2

# functions for computer


def count(dice, number):  # counts how many times a specific number is in the dice
    count = 0
    for i in dice:
        if i[0] == number:
            count += 1
    return count


# returns the place and number of maximum points posible with the dice
def max_here(points, options, options_player):
    j = -1
    maximum = -1
    for i in range(len(options)):
        if options[i] in options_player:
            if points[i] >= maximum:
                maximum = points[i]
                j = i
    return maximum, j


def similar(dice):  # returns the number of times that the dice show same number
    maximum = 0
    for i in range(len(dice)):
        counter = 1
        for j in range(1, len(dice)):
            if i != j:
                if dice[i] == dice[j]:
                    counter += 1
        if counter > maximum:
            maximum = counter
    return maximum


def keep_number(dice, number):  # turns the number input to true every time its in the dice
    for i in range(len(dice)):
        if int(dice[i][0]) == int(number):
            dice[i][1] = True
    return dice


def common(dice, options_player):  # returns the common number in the dice
    common = 0
    number = -1
    for i in range(1, 7):
        if str(i) in options_player:
            counter = 0
            for j in dice:
                if i == j[0]:
                    counter += 1
            if common <= counter:
                common = counter
                number = i
    return number


def common_to_end(dice):
    common = 0
    number = -1
    for i in range(1, 7):
        counter = 0
        for j in dice:
            if i == j[0]:
                counter += 1
        if common <= counter:
            common = counter
            number = i
    return number


# if its special it keeps all the numbers else it keeps the most common number if on the options for the player
def choose_what_to_keep(number, dice, options_player):
    if yatzy(dice) != 0:
        if "yatzy" in options_player:
            for i in range(len(dice)):
                dice[i][1] = True
    if full_house(dice) != 0:
        if "full house" in options_player:
            for i in range(len(dice)):
                dice[i][1] = True
    if long(dice) != 0:
        if "big" in options_player:
            for i in range(len(dice)):
                dice[i][1] = True
    if small(dice) != 0:
        if "small" in options_player:
            for i in range(len(dice)):
                dice[i][1] = True
    if 0 <= number <= 6:
        for i in range(len(dice)):
            if int(dice[i][0]) == int(number):
                dice[i][1] = True
    elif number == 7:
        if count(dice, 5) > count(dice, 6):
            for i in dice:
                if i[0] == 5:
                    i[1] == True
        else:
            for i in dice:
                if i[0] == 6:
                    i[1] == True
    elif number == 8 or number == 9:
        temp = common(dice, options_player)
        dice = keep_number(dice, temp)
    return dice


def prefer(options_player, options, choose):
    if choose in options_player:
        for i in range(len(options_player)):
            if options_player[i] == choose:
                return i
    return -1


# helps to check if there is a special sequence on the dice
def choose_special(dice, options_player, special, points_player):
    if special in options_player:
        for j in range(len(options)):
            if options[j] == special:
                temp = j
        if special == "second yatzy":
            if points_player[temp+1] != 0:
                for i in range(len(options_player)):
                    if options_player[i] == special:
                        return i
        else:
            if points_player[temp] != 0:
                for i in range(len(options_player)):
                    if options_player[i] == special:
                        return i
    return -1


def find(play, options_player):  # find the location of a str from options in options_player
    for i in range(len(options_player)):
        if str(play) == options_player[i]:
            return i
    return -1
