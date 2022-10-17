
import random
import PySimpleGUI as sg
import pickle
#functios for points
def one (dices):
    count = 0
    for i in dices:
        if i[0] == 1:
            count += 1
    return count


def two(dices):
    count = 0
    for i in dices:
        if i[0] == 2:
            count += 1
    return count*2


def three(dices):
    count = 0
    for i in dices:
        if i[0] == 3:
            count += 1
    return count*3


def four(dices):
    count = 0
    for i in dices:
        if i[0] == 4:
            count += 1
    return count*4


def five(dices):
    count = 0
    for i in dices:
        if i[0] == 5:
            count += 1
    return count*5


def six(dices):
    count = 0
    for i in dices:
        if i[0] == 6:
            count += 1
    return count*6


def X3(dices):
    dices0 = list(dices)
    dices0.sort()
    if dices0[0][0] == dices0[1][0] == dices0[2][0] or dices0[2][0] == dices0[3][0] == dices0[4][0] or dices0[1][0] == dices0[2][0] == dices0[3][0]:
        return sum(row[0] for row in dices)
    return 0


def X4(dices):
    dices0 = list(dices)
    dices0.sort()
    if dices0[0][0] == dices0[1][0] == dices0[2][0] == dices0[3][0] or dices0[1][0] == dices0[2][0] == dices0[3][0] == dices0[4][0]:
        return sum(row[0] for row in dices)
    return 0


def full_house(dices):
    dices0 = list(dices)
    dices0.sort()
    if dices0[0][0] == dices0[1][0] == dices0[2][0] and dices0[2][0] != dices0[3][0] == dices0[4][0]:
        return 25
    if dices0[0][0] == dices0[1][0] != dices0[2][0] and dices0[2][0] == dices0[3][0] == dices0[4][0]:
        return 25
    return 0


def small(dices):
    dices0 = list(dices)
    dices0.sort()
    if dices0[4][0] == dices0[3][0]+1 == dices0[2][0]+2 == dices0[1][0]+3 or dices0[3][0] == dices0[2][0]+1 == dices0[1][0]+2 == dices0[0][0]+3:
        return 30
    if dices0[3][0] == dices0[2][0]:
        if dices0[4][0] == dices0[2][0]+1 == dices0[1][0]+2 == dices0[0][0]+3:
            return 30
    if dices0[2][0] == dices0[1][0]:
        if dices0[4][0] == dices0[3][0]+1 == dices0[1][0]+2 == dices0[0][0]+3:
            return 30
    return 0


def long(dices):
    dices0 = list(dices)
    dices0.sort()
    if dices0[4][0] == dices0[3][0]+1 == dices0[2][0]+2 == dices0[1][0]+3 == dices0[0][0]+4:
        return 40
    return 0


def yatzy(dices):
    if dices[0][0] == dices[1][0] == dices[2][0] == dices[3][0] == dices[4][0]:
        return 50
    return 0


def check_for_bonus(score):
    if sum(score[0:6]) > 63:
        score[13] = 35
    return score


def show_points(score, temp, points, dices):
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


def change_dices(dices, turn, window, tries):
    if dices[0][1] == False:
        dices[0][0] = random.randint(1, 6)
    else:
        dices[0][1] = True
    if dices[1][1] == False:
        dices[1][0] = random.randint(1, 6)
    else:
        dices[1][1] = True
    if dices[2][1] == False:
        dices[2][0] = random.randint(1, 6)
    else:
        dices[2][1] = True
    if dices[3][1] == False:
        dices[3][0] = random.randint(1, 6)
    else:
        dices[3][1] = True
    if dices[4][1] == False:
        dices[4][0] = random.randint(1, 6)
    else:
        dices[4][1] = True
    return dices

# functions to build screen
def new_screen(score_player1, score_player2, options_player1, options_player2, counter_player1, counter_player2, dices_player1, dices_player2, points_player1, points_player2, turn, tries):
    if turn == 0:
        pl1 = (show_points(score_player1, [
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], points_player1, dices_player1))
        pl2 = score_player2
        if tries <= 2:
            layout = [[sg.Text("player1", visible=True), (sg.Text("\t\t        player2", visible=True, key="name_2"))],
                      [(sg.Text("player 1 score: "+str(sum(score_player1)))),
                       (sg.Text("\t         player 2 score: "+str(sum(score_player2))))],
                      [(sg.Checkbox(dices_player1[0][0], visible=True, default=dices_player1[0][1], key="1")), (sg.Checkbox(dices_player1[1][0], visible=True, default=dices_player1[1][1], key="2")), (sg.Checkbox(dices_player1[2][0], visible=True, default=dices_player1[2][1], key="3")),
                       (sg.Checkbox(dices_player1[3][0], visible=True, default=dices_player1[3][1], key="4")), (sg.Checkbox(
                           dices_player1[4][0], visible=True, default=dices_player1[4][1], key="5")), sg.Text("\t\t              "),
                       (sg.Checkbox(dices_player2[0][0], visible=False, default=dices_player2[0][1], key="6")), (sg.Checkbox(
                           dices_player2[1][0], visible=False, default=dices_player2[1][1], key="7")), (sg.Checkbox(dices_player2[2][0], visible=False, default=dices_player2[2][1], key="8")),
                       (sg.Checkbox(dices_player2[3][0], visible=False, default=dices_player2[3][1], key="9")), sg.Checkbox(dices_player2[4][0], visible=False, default=dices_player2[4][1], key="10")],
                      [(sg.Text("1: " + str(pl1[0]), key="a1")), (sg.Text("  X3: " + str(pl1[6]), key="a2")), (sg.Text(
                          "       \t          1: " + str(pl2[0]), key="b1")), (sg.Text("  X3: " + str(pl2[6]), key="b2"))],
                      [(sg.Text("2: "+str(pl1[1]), key="a3")), (sg.Text("  X4: " + str(pl1[7]), key="a4")), (sg.Text(
                          "           \t          2: "+str(pl2[1]), key="b3")), (sg.Text("  X4: " + str(pl2[7]), key="b4"))],
                      [(sg.Text("3: " + str(pl1[2]), key="a5")), (sg.Text("  full house: " + str(pl1[8]), key="a6")),
                       (sg.Text("        \t3: " + str(pl2[2]), key="b5")), (sg.Text("  full house: " + str(pl2[8]), key="b6"))],
                      [(sg.Text("4: " + str(pl1[3]), key="a7")), (sg.Text("  small straight: " + str(pl1[9]), key="a8")),
                       (sg.Text("        4: " + str(pl2[3]), key="b7")), (sg.Text("  small straight: " + str(pl2[9]), key="b8"))],
                      [(sg.Text("5: " + str(pl1[4]), key="a9")), (sg.Text("  big sraight: " + str(pl1[10]), key="a10")),
                       (sg.Text("            5: " + str(pl2[4]), key="b9")), (sg.Text("  big sraight: " + str(pl2[10]), key="b10"))],
                      [(sg.Text("6: " + str(pl1[5]), key="a11")), (sg.Text("  yatzy: " + str(pl1[11]), key="a12")),
                       (sg.Text("\t      6: " + str(pl2[5]), key="b11")), (sg.Text("  yatzy: " + str(pl2[11]), key="b12"))],
                      [(sg.Text("sum: " + str(pl1[12]), key="a13")), sg.Text("second yatzy: " + str(pl1[14]), key="a14"),
                       (sg.Text("     sum: " + str(pl2[12]), key="b13")), sg.Text("second yatzy: " + str(pl2[14]), key="b14")],
                      [sg.Text("bonus under\over: " + str(pl1[13])), sg.Text("         "),
                       sg.Text("bonus under\over: " + str(pl2[13]))],
                      [(sg.Text("\t\t    ")), (sg.Button("next", bind_return_key=True))]]
            return layout
        else:
            layout = [[sg.Text("player1", visible=True), (sg.Text("\t\t        player2", visible=True, key="name_2"))],
                      [(sg.Text("player 1 score: "+str(sum(score_player1)))),
                       (sg.Text("\t         player 2 score: "+str(sum(score_player2))))],
                      [(sg.Checkbox(dices_player1[0][0], visible=True, default=dices_player1[0][1], key="1")), (sg.Checkbox(dices_player1[1][0], visible=True, default=dices_player1[1][1], key="2")), (sg.Checkbox(dices_player1[2][0], visible=True, default=dices_player1[2][1], key="3")),
                       (sg.Checkbox(dices_player1[3][0], visible=True, default=dices_player1[3][1], key="4")), (sg.Checkbox(
                           dices_player1[4][0], visible=True, default=dices_player1[4][1], key="5")), sg.Text("\t\t              "),
                       (sg.Checkbox(dices_player2[0][0], visible=False, default=dices_player2[0][1], key="6")), (sg.Checkbox(
                           dices_player2[1][0], visible=False, default=dices_player2[1][1], key="7")), (sg.Checkbox(dices_player2[2][0], visible=False, default=dices_player2[2][1], key="8")),
                       (sg.Checkbox(dices_player2[3][0], visible=False, default=dices_player2[3][1], key="9")), sg.Checkbox(dices_player2[4][0], visible=False, default=dices_player2[4][1], key="10")],
                      [(sg.Text("1: " + str(pl1[0]), key="a1")), (sg.Text("  X3: " + str(pl1[6]), key="a2")), (sg.Text(
                          "       \t          1: " + str(pl2[0]), key="b1")), (sg.Text("  X3: " + str(pl2[6]), key="b2"))],
                      [(sg.Text("2: "+str(pl1[1]), key="a3")), (sg.Text("  X4: " + str(pl1[7]), key="a4")), (sg.Text(
                          "           \t          2: "+str(pl2[1]), key="b3")), (sg.Text("  X4: " + str(pl2[7]), key="b4"))],
                      [(sg.Text("3: " + str(pl1[2]), key="a5")), (sg.Text("  full house: " + str(pl1[8]), key="a6")),
                       (sg.Text("        \t3: " + str(pl2[2]), key="b5")), (sg.Text("  full house: " + str(pl2[8]), key="b6"))],
                      [(sg.Text("4: " + str(pl1[3]), key="a7")), (sg.Text("  small straight: " + str(pl1[9]), key="a8")),
                       (sg.Text("        4: " + str(pl2[3]), key="b7")), (sg.Text("  small straight: " + str(pl2[9]), key="b8"))],
                      [(sg.Text("5: " + str(pl1[4]), key="a9")), (sg.Text("  big sraight: " + str(pl1[10]), key="a10")),
                       (sg.Text("            5: " + str(pl2[4]), key="b9")), (sg.Text("  big sraight: " + str(pl2[10]), key="b10"))],
                      [(sg.Text("6: " + str(pl1[5]), key="a11")), (sg.Text("  yatzy: " + str(pl1[11]), key="a12")),
                       (sg.Text("\t      6: " + str(pl2[5]), key="b11")), (sg.Text("  yatzy: " + str(pl2[11]), key="b12"))],
                      [(sg.Text("sum: " + str(pl1[12]), key="a13")), sg.Text("second yatzy: " + str(pl1[14]), key="a14"),
                       (sg.Text("     sum: " + str(pl2[12]), key="b13")), sg.Text("second yatzy: " + str(pl2[14]), key="b14")],
                      [sg.Text("bonus under\over: " + str(pl1[13])), sg.Text("         "),
                       sg.Text("bonus under\over: " + str(pl2[13]))],
                      [(sg.Text("\t\t    ")), (sg.Button("next", bind_return_key=True))]]
            return layout
    if turn == 1:
        if tries <= 2:
            pl1 = score_player1
            pl2 = (show_points(score_player2, [
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], points_player2, dices_player2))
            layout = [[sg.Text("player1", visible=True), (sg.Text("\t\t        player2", visible=True, key="name_2"))],
                      [(sg.Text("player 1 score: "+str(sum(score_player1)))),
                       (sg.Text("\t         player 2 score: "+str(sum(score_player2))))],
                      [(sg.Checkbox(dices_player1[0][0], visible=False, default=dices_player1[0][1], key="1")), (sg.Checkbox(dices_player1[1][0], visible=False, default=dices_player1[1][1], key="2")), (sg.Checkbox(dices_player1[2][0], visible=False, default=dices_player1[2][1], key="3")),
                       (sg.Checkbox(dices_player1[3][0], visible=False, default=dices_player1[3][1], key="4")), (sg.Checkbox(
                           dices_player1[4][0], visible=False, default=dices_player1[4][1], key="5")), sg.Text("\t\t              "),
                       (sg.Checkbox(dices_player2[0][0], visible=True, default=dices_player2[0][1], key="6")), (sg.Checkbox(
                           dices_player2[1][0], visible=True, default=dices_player2[1][1], key="7")), (sg.Checkbox(dices_player2[2][0], visible=True, default=dices_player2[2][1], key="8")),
                       (sg.Checkbox(dices_player2[3][0], visible=True, default=dices_player2[3][1], key="9")), sg.Checkbox(dices_player2[4][0], visible=True, default=dices_player2[4][1], key="10")],
                      [(sg.Text("1: " + str(pl1[0]), key="a1")), (sg.Text("  X3: " + str(pl1[6]), key="a2")), (sg.Text(
                          "       \t          1: " + str(pl2[0]), key="b1")), (sg.Text("  X3: " + str(pl2[6]), key="b2"))],
                      [(sg.Text("2: "+str(pl1[1]), key="a3")), (sg.Text("  X4: " + str(pl1[7]), key="a4")), (sg.Text(
                          "           \t          2: "+str(pl2[1]), key="b3")), (sg.Text("  X4: " + str(pl2[7]), key="b4"))],
                      [(sg.Text("3: " + str(pl1[2]), key="a5")), (sg.Text("  full house: " + str(pl1[8]), key="a6")),
                       (sg.Text("        \t3: " + str(pl2[2]), key="b5")), (sg.Text("  full house: " + str(pl2[8]), key="b6"))],
                      [(sg.Text("4: " + str(pl1[3]), key="a7")), (sg.Text("  small straight: " + str(pl1[9]), key="a8")),
                       (sg.Text("        4: " + str(pl2[3]), key="b7")), (sg.Text("  small straight: " + str(pl2[9]), key="b8"))],
                      [(sg.Text("5: " + str(pl1[4]), key="a9")), (sg.Text("  big sraight: " + str(pl1[10]), key="a10")),
                       (sg.Text("            5: " + str(pl2[4]), key="b9")), (sg.Text("  big sraight: " + str(pl2[10]), key="b10"))],
                      [(sg.Text("6: " + str(pl1[5]), key="a11")), (sg.Text("  yatzy: " + str(pl1[11]), key="a12")),
                       (sg.Text("\t      6: " + str(pl2[5]), key="b11")), (sg.Text("  yatzy: " + str(pl2[11]), key="b12"))],
                      [(sg.Text("sum: " + str(pl1[12]), key="a13")), sg.Text("second yatzy: " + str(pl1[14]), key="a14"),
                       (sg.Text("     sum: " + str(pl2[12]), key="b13")), sg.Text("second yatzy: " + str(pl2[14]), key="b14")],
                      [sg.Text("bonus under\over: " + str(pl1[13])), sg.Text("         "),
                       sg.Text("bonus under\over: " + str(pl2[13]))],
                      [(sg.Text("\t\t    ")), (sg.Button("next", bind_return_key=True))]]
            return layout
        else:
            pl1 = score_player1
            pl2 = (show_points(score_player2, [
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], points_player2, dices_player2))
            layout = [[sg.Text("player1", visible=True), (sg.Text("\t\t        player2", visible=True, key="name_2"))],
                      [(sg.Text("player 1 score: "+str(sum(score_player1)))),
                       (sg.Text("\t         player 2 score: "+str(sum(score_player2))))],
                      [(sg.Checkbox(dices_player1[0][0], visible=False, default=dices_player1[0][1], key="1")), (sg.Checkbox(dices_player1[1][0], visible=False, default=dices_player1[1][1], key="2")), (sg.Checkbox(dices_player1[2][0], visible=False, default=dices_player1[2][1], key="3")),
                       (sg.Checkbox(dices_player1[3][0], visible=False, default=dices_player1[3][1], key="4")), (sg.Checkbox(
                           dices_player1[4][0], visible=False, default=dices_player1[4][1], key="5")), sg.Text("\t\t              "),
                       (sg.Checkbox(dices_player2[0][0], visible=True, default=dices_player2[0][1], key="6")), (sg.Checkbox(
                           dices_player2[1][0], visible=True, default=dices_player2[1][1], key="7")), (sg.Checkbox(dices_player2[2][0], visible=True, default=dices_player2[2][1], key="8")),
                       (sg.Checkbox(dices_player2[3][0], visible=True, default=dices_player2[3][1], key="9")), sg.Checkbox(dices_player2[4][0], visible=True, default=dices_player2[4][1], key="10")],
                      [(sg.Text("1: " + str(pl1[0]), key="a1")), (sg.Text("  X3: " + str(pl1[6]), key="a2")), (sg.Text(
                          "       \t          1: " + str(pl2[0]), key="b1")), (sg.Text("  X3: " + str(pl2[6]), key="b2"))],
                      [(sg.Text("2: "+str(pl1[1]), key="a3")), (sg.Text("  X4: " + str(pl1[7]), key="a4")), (sg.Text(
                          "           \t          2: "+str(pl2[1]), key="b3")), (sg.Text("  X4: " + str(pl2[7]), key="b4"))],
                      [(sg.Text("3: " + str(pl1[2]), key="a5")), (sg.Text("  full house: " + str(pl1[8]), key="a6")),
                       (sg.Text("        \t3: " + str(pl2[2]), key="b5")), (sg.Text("  full house: " + str(pl2[8]), key="b6"))],
                      [(sg.Text("4: " + str(pl1[3]), key="a7")), (sg.Text("  small straight: " + str(pl1[9]), key="a8")),
                       (sg.Text("        4: " + str(pl2[3]), key="b7")), (sg.Text("  small straight: " + str(pl2[9]), key="b8"))],
                      [(sg.Text("5: " + str(pl1[4]), key="a9")), (sg.Text("  big sraight: " + str(pl1[10]), key="a10")),
                       (sg.Text("            5: " + str(pl2[4]), key="b9")), (sg.Text("  big sraight: " + str(pl2[10]), key="b10"))],
                      [(sg.Text("6: " + str(pl1[5]), key="a11")), (sg.Text("  yatzy: " + str(pl1[11]), key="a12")),
                       (sg.Text("\t      6: " + str(pl2[5]), key="b11")), (sg.Text("  yatzy: " + str(pl2[11]), key="b12"))],
                      [(sg.Text("sum: " + str(pl1[12]), key="a13")), sg.Text("second yatzy: " + str(pl1[14]), key="a14"),
                       (sg.Text("     sum: " + str(pl2[12]), key="b13")), sg.Text("second yatzy: " + str(pl2[14]), key="b14")],
                      [sg.Text("bonus under\over: " + str(pl1[13])), sg.Text("         "),
                       sg.Text("bonus under\over: " + str(pl2[13]))],
                      [(sg.Text("\t\t    ")), (sg.Button("next", bind_return_key=True))]]
            return layout

#functions to give points after choose
def ok_choose(turn, score_player1, score_player2, dices_player1, dices_player2, options_player1, options_player2, place1, place2):
    if turn == 0:
        if place1 == "1":
            score_player1[0] = one(dices_player1)
            options_player1.remove("1")
        if place1 == "2":
            score_player1[1] = two(dices_player1)
            options_player1.remove("2")
        if place1 == "3":
            score_player1[2] = three(dices_player1)
            options_player1.remove("3")
        if place1 == "4":
            score_player1[3] = four(dices_player1)
            options_player1.remove("4")
        if place1 == "5":
            score_player1[4] = five(dices_player1)
            options_player1.remove("5")
        if place1 == "6":
            score_player1[5] = six(dices_player1)
            options_player1.remove("6")
        if place1 == "x3":
            score_player1[6] = X3(dices_player1)
            options_player1.remove("x3")
        if place1 == "x4":
            score_player1[7] = X4(dices_player1)
            options_player1.remove("x4")
        if place1 == "full house":
            score_player1[8] = full_house(dices_player1)
            options_player1.remove("full house")
        if place1 == "small":
            score_player1[9] = small(dices_player1)
            options_player1.remove("small")
        if place1 == "big":
            score_player1[10] = long(dices_player1)
            options_player1.remove("big")
        if place1 == "yatzy":
            score_player1[11] = yatzy(dices_player1)
            options_player1.remove("yatzy")
        if place1 == "sum":
            score_player1[12] = sum(row[0] for row in dices_player1)
            options_player1.remove("sum")
        if place1 == "second yatzy":
            if score_player1[11] != 0:
                score_player1[14] = yatzy(dices_player1)
            options_player1.remove("second yatzy")
    else:
        if place2 == "1":
            score_player2[0] = one(dices_player2)
            options_player2.remove("1")
        if place2 == "2":
            score_player2[1] = two(dices_player2)
            options_player2.remove("2")
        if place2 == "3":
            score_player2[2] = three(dices_player2)
            options_player2.remove("3")
        if place2 == "4":
            score_player2[3] = four(dices_player2)
            options_player2.remove("4")
        if place2 == "5":
            score_player2[4] = five(dices_player2)
            options_player2.remove("5")
        if place2 == "6":
            score_player2[5] = six(dices_player2)
            options_player2.remove("6")
        if place2 == "x3":
            score_player2[6] = X3(dices_player2)
            options_player2.remove("x3")
        if place2 == "x4":
            score_player2[7] = X4(dices_player2)
            options_player2.remove("x4")
        if place2 == "full house":
            score_player2[8] = full_house(dices_player2)
            options_player2.remove("full house")
        if place2 == "small":
            score_player2[9] = small(dices_player2)
            options_player2.remove("small")
        if place2 == "big":
            score_player2[10] = long(dices_player2)
            options_player2.remove("big")
        if place2 == "yatzy":
            score_player2[11] = yatzy(dices_player2)
            options_player2.remove("yatzy")
        if place2 == "sum":
            score_player2[12] = sum(row[0] for row in dices_player2)
            options_player2.remove("sum")
        if place2 == "second yatzy":
            if score_player2[11] != 0:
                score_player2[14] = yatzy(dices_player2)
            options_player2.remove("second yatzy")
    return options_player1, options_player2, score_player1, score_player2

# functions for computer

def count(dices, number):#counts how many times a specific number is in the dices
    count = 0
    for i in dices:
        if i[0] == number:
            count += 1
    return count


def max_here(points, options, options_player): #returns the place and number of maximum points posible with the dices
    j = -1
    maximum = -1
    for i in range(len(options)):
        if options[i] in options_player:
            if points[i] >= maximum:
                maximum = points[i]
                j = i
    return maximum, j


def similar(dices): #returns the number of times that the dices show same number
    maximum = 0
    for i in range(len(dices)):
        counter = 1
        for j in range(1, len(dices)):
            if i != j:
                if dices[i] == dices[j]:
                    counter += 1
        if counter > maximum:
            maximum = counter
    return maximum


def keep_number(dices, number):# turns the number input to true every time its in the dices
    for i in range(len(dices)):
        if int(dices[i][0]) == int(number):
            dices[i][1] = True
    return dices


def common(dices, options_player):#returns the common number in the dices
    common = 0
    number = -1
    for i in range(1, 7):
        if str(i) in options_player:
            counter = 0
            for j in dices:
                if i == j[0]:
                    counter += 1
            if common <= counter:
                common = counter
                number = i
    return number

def common_to_end(dices):
    common = 0
    number = -1
    for i in range(1, 7):
        counter = 0
        for j in dices:
            if i == j[0]:
                counter += 1
        if common <= counter:
            common = counter
            number = i
    return number

def choose_what_to_keep(number, dices, options_player):# if its speicel it keeps all the numbers else it keeps the most common number if on the options for the player
    if yatzy(dices) != 0:
        if "yatzy" in options_player:
            for i in range(len(dices)):
                dices[i][1] = True
    if full_house(dices) != 0:
        if "full house" in options_player:
            for i in range(len(dices)):
                dices[i][1] = True
    if long(dices) != 0:
        if "big" in options_player:
            for i in range(len(dices)):
                dices[i][1] = True
    if small(dices) != 0:
        if "small" in options_player:
            for i in range(len(dices)):
                dices[i][1] = True
    if 0 <= number <= 6:
        for i in range(len(dices)):
            if int(dices[i][0]) == int(number):
                dices[i][1] = True
    elif number == 7:
        if count(dices, 5) > count(dices, 6):
            for i in dices:
                if i[0] == 5:
                    i[1] == True
        else:
            for i in dices:
                if i[0] == 6:
                    i[1] == True
    elif number == 8 or number == 9:
        temp = common(dices, options_player)
        dices = keep_number(dices, temp)
    return dices


def prefer(options_player, options, choose):
    if choose in options_player:
        for i in range(len(options_player)):
            if options_player[i] == choose:
                return i
    return -1


def choose_speicel(dices, options_player, speicel, points_player):# helps to check if there is a speicel sequense on the dices
    if speicel in options_player:
        for j in range(len(options)):
            if options[j] == speicel:
                temp = j
        if speicel=="second yatzy":
            if points_player[temp+1] != 0:
                for i in range(len(options_player)):
                    if options_player[i] == speicel:
                        return i
        else:
            if points_player[temp] != 0:
                for i in range(len(options_player)):
                    if options_player[i] == speicel:
                        return i
    return -1


def find(play, options_player):#find the location of a str from options in options_player
    for i in range(len(options_player)):
        if str(play) == options_player[i]:
            return i
    return -1


# game starts here
score_player1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
score_player2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 0
end = 0
options = ["1", "2", "3", "4", "5", "6", "x3", "x4","full house", "small", "big", "yatzy", "sum", "second yatzy"]
options_player1 = ["1", "2", "3", "4", "5", "6", "x3", "x4","full house", "small", "big", "yatzy", "sum", "second yatzy"]
options_player2 = ["1", "2", "3", "4", "5", "6", "x3", "x4","full house", "small", "big", "yatzy", "sum", "second yatzy"]
counter_player1 = sum(score_player1[0:6])
counter_player2 = sum(score_player2[0:6])
tries = 1
play = 0

sg.SetOptions(element_padding=(5, 9), font=('Verdana', 14),
              input_elements_background_color='#27F727', input_text_color='#ffffff')  # Add a touch of color
for i in range(26):
    tries = 1
    temp = 7
    flag = -1
    dices_player1 = [[random.randint(1, 6), False], [random.randint(1, 6), False], [random.randint(1, 6), False], [random.randint(1, 6), False], [random.randint(1, 6), False]]
    dices_player2 = [[random.randint(1, 6), False], [random.randint(1, 6), False], [random.randint(1, 6), False], [random.randint(1, 6), False], [random.randint(1, 6), False]]
    # if i==20:
    #      dices_player1=[[1,False],[2,False],[3,False],[4,False],[5,False]]
    points_player1 = [one(dices_player1), two(dices_player1), three(dices_player1), four(dices_player1), five(dices_player1), six(dices_player1), X3(dices_player1), X4(dices_player1), full_house(dices_player1), small(dices_player1), long(dices_player1), yatzy(dices_player1), sum(row[0] for row in dices_player1), bonus(score_player1, options_player1, options), yatzy(dices_player1)]
    points_player2 = [one(dices_player2), two(dices_player2), three(dices_player2), four(dices_player2), five(dices_player2), six(dices_player2), X3(dices_player2), X4(dices_player2), full_house(dices_player2), small(dices_player2), long(dices_player2), yatzy(dices_player2), sum(row[0] for row in dices_player2), bonus(score_player2, options_player2, options), yatzy(dices_player2)]
    layout = new_screen(score_player1, score_player2, options_player1, options_player2, counter_player1,counter_player2, dices_player1, dices_player2, points_player1, points_player2, turn, tries)
    window = sg.Window('game', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break
        if event == "next":
            if turn == 0:
                window.close()
                play = common(dices_player1, options_player1)
                if end ==1:
                    play = common_to_end(dices_player1)
                    print(play)
                dices_player1 = choose_what_to_keep(play, dices_player1, options_player1)
                dices_player1 = change_dices(dices_player1, turn, window, tries)
                points_player1 = [one(dices_player1), two(dices_player1), three(dices_player1), four(dices_player1), five(dices_player1), six(dices_player1), X3(dices_player1), X4(dices_player1), full_house(dices_player1), small(dices_player1), long(dices_player1), yatzy(dices_player1), sum(row[0] for row in dices_player1), bonus(score_player1, options_player1, options), yatzy(dices_player1)]
                points_player2 = [one(dices_player2), two(dices_player2), three(dices_player2), four(dices_player2), five(dices_player2), six(dices_player2), X3(dices_player2), X4(dices_player2), full_house(dices_player2), small(dices_player2), long(dices_player2), yatzy(dices_player2), sum(row[0] for row in dices_player2), bonus(score_player2, options_player2, options), yatzy(dices_player2)]
                layout = new_screen(score_player1, score_player2, options_player1, options_player2, counter_player1,counter_player2, dices_player1, dices_player2, points_player1, points_player2, turn, tries)
                window = sg.Window('game', layout)
                while True:
                    event, values = window.read()
                    if event == "next":
                        window.close()
                        play = common(dices_player1, options_player1)
                        if end ==1:
                            play = common_to_end(dices_player1)
                            print(play)
                        dices_player1 = choose_what_to_keep(play, dices_player1, options_player1)
                        dices_player1 = change_dices(dices_player1, turn, window, tries)
                        points_player1 = [one(dices_player1), two(dices_player1), three(dices_player1), four(dices_player1), five(dices_player1), six(dices_player1), X3(dices_player1), X4(dices_player1), full_house(dices_player1), small(dices_player1), long(dices_player1), yatzy(dices_player1), sum(row[0] for row in dices_player1), bonus(score_player1, options_player1, options), yatzy(dices_player1)]
                        points_player2 = [one(dices_player2), two(dices_player2), three(dices_player2), four(dices_player2), five(dices_player2), six(dices_player2), X3(dices_player2), X4(dices_player2), full_house(dices_player2), small(dices_player2), long(dices_player2), yatzy(dices_player2), sum(row[0] for row in dices_player2), bonus(score_player2, options_player2, options), yatzy(dices_player2)]
                        layout = new_screen(score_player1, score_player2, options_player1, options_player2, counter_player1,counter_player2, dices_player1, dices_player2, points_player1, points_player2, turn, tries)
                        window = sg.Window('game', layout)
                        while True:
                            event, values = window.read()
                            if event == "next":
                                points_player1 = [one(dices_player1), two(dices_player1), three(dices_player1), four(dices_player1), five(dices_player1), six(dices_player1), X3(dices_player1), X4(dices_player1), full_house(dices_player1), small(dices_player1), long(dices_player1), yatzy(dices_player1), sum(row[0] for row in dices_player1), bonus(score_player1, options_player1, options), yatzy(dices_player1)]
                                com1, place1 = max_here(points_player1, options, options_player1)
                                for i in options[8:12]:
                                    if choose_speicel(dices_player1, options_player1, i, points_player1) != -1:
                                        flag = choose_speicel(dices_player1, options_player1, i, points_player1)
                                if score_player1[11]!=0:        
                                        if choose_speicel(dices_player1, options_player1, "second yatzy", points_player1)!=-1:
                                            flag = choose_speicel(dices_player1, options_player1, "second yatzy", points_player1)
                                if flag == -1:
                                    play = find(play, options_player1)
                                    if play == -1:
                                        end = 1
                                        com1, place1 = max_here(points_player1, options, options_player1)
                                        play = find(options[place1],options_player1)
                                    options_player1, options_player2, score_player1, score_player2 = ok_choose(turn, score_player1, score_player2, dices_player1, dices_player2, options_player1, options_player2, options_player1[play], options[place1])
                                else:
                                    options_player1, options_player2, score_player1, score_player2 = ok_choose(
                                        turn, score_player1, score_player2, dices_player1, dices_player2, options_player1, options_player2, options_player1[flag], options[place1])
                                break
                        break
                #com1, place1 = max_here(points_player1,options,options_player1)
                #options_player1, options_player2 , score_player1,score_player2 =ok_choose(turn,score_player1,score_player2,dices_player1,dices_player2,options_player1,options_player2,options[place1],options[play])
            if turn == 1:
                window.close()
                play = common(dices_player2, options_player2)
                if play == 1:
                    if count(dices_player2, play) == 4:
                        dices_player2 = choose_what_to_keep(
                            play, dices_player2, options_player2)
                        dices_player2 = change_dices(
                            dices_player2, turn, window, tries)
                    else:
                        dices_player2 = change_dices(
                            dices_player2, turn, window, tries)
                if 2 <= play <= 6:
                    #dices_player2 = keep_number(dices_player2,play)
                    dices_player2 = choose_what_to_keep(
                        play, dices_player2, options_player2)
                    dices_player2 = change_dices(
                        dices_player2, turn, window, tries)
                if play == -1:
                    play = temp
                    dices_player2 = choose_what_to_keep(
                        play, dices_player2, options_player2)
                    dices_player2 = change_dices(
                        dices_player2, turn, window, tries)
                points_player1 = [one(dices_player1), two(dices_player1), three(dices_player1), four(dices_player1), five(dices_player1), six(dices_player1), X3(dices_player1), X4(dices_player1), full_house(
                    dices_player1), small(dices_player1), long(dices_player1), yatzy(dices_player1), sum(row[0] for row in dices_player1), bonus(score_player1, options_player1, options), yatzy(dices_player1)]
                points_player2 = [one(dices_player2), two(dices_player2), three(dices_player2), four(dices_player2), five(dices_player2), six(dices_player2), X3(dices_player2), X4(dices_player2), full_house(
                    dices_player2), small(dices_player2), long(dices_player2), yatzy(dices_player2), sum(row[0] for row in dices_player2), bonus(score_player2, options_player2, options), yatzy(dices_player2)]
                layout = new_screen(score_player1, score_player2, options_player1, options_player2, counter_player1,
                                    counter_player2, dices_player1, dices_player2, points_player1, points_player2, turn, tries)
                window = sg.Window('game', layout)
                while True:
                    event, values = window.read()
                    if event == "next":
                        window.close()
                        play = common(dices_player2, options_player2)
                        if 2 <= play <= 6:
                            dices_player2 = choose_what_to_keep(
                                play, dices_player2, options_player2)
                            dices_player2 = change_dices(
                                dices_player2, turn, window, tries)
                        if play == -1:
                            play = temp
                            dices_player2 = choose_what_to_keep(
                                play, dices_player2, options_player2)
                            dices_player2 = change_dices(
                                dices_player2, turn, window, tries)
                        points_player1 = [one(dices_player1), two(dices_player1), three(dices_player1), four(dices_player1), five(dices_player1), six(dices_player1), X3(dices_player1), X4(dices_player1), full_house(
                            dices_player1), small(dices_player1), long(dices_player1), yatzy(dices_player1), sum(row[0] for row in dices_player1), bonus(score_player1, options_player1, options), yatzy(dices_player1)]
                        points_player2 = [one(dices_player2), two(dices_player2), three(dices_player2), four(dices_player2), five(dices_player2), six(dices_player2), X3(dices_player2), X4(dices_player2), full_house(
                            dices_player2), small(dices_player2), long(dices_player2), yatzy(dices_player2), sum(row[0] for row in dices_player2), bonus(score_player2, options_player2, options), yatzy(dices_player2)]
                        layout = new_screen(score_player1, score_player2, options_player1, options_player2, counter_player1,
                                            counter_player2, dices_player1, dices_player2, points_player1, points_player2, turn, tries)
                        window = sg.Window('game', layout)
                        while True:
                            event, values = window.read()
                            if event == "next":
                                points_player2 = [one(dices_player2), two(dices_player2), three(dices_player2), four(dices_player2), five(dices_player2), six(dices_player2), X3(dices_player2), X4(dices_player2), full_house(
                                    dices_player2), small(dices_player2), long(dices_player2), yatzy(dices_player2), sum(row[0] for row in dices_player2), bonus(score_player2, options_player2, options), yatzy(dices_player2)]
                                com2, place2 = max_here(
                                    points_player2, options, options_player2)
                                options_player1, options_player2, score_player1, score_player2 = ok_choose(turn, score_player1, score_player2, dices_player1, dices_player2, options_player1, options_player2, options[place2], options[place2])
                                break
                        break
                    temp += 1
                #com2, place2 = max_here(points_player2,options,options_player2)
            turn = (turn + 1) % 2
            break
    counter_player1 = sum(score_player1[0:6])
    counter_player2 = sum(score_player2[0:6])
    if counter_player1 >= 63:
        score_player1[13] = 35
    if counter_player2 >= 63:
        score_player2[13] = 35
    window.close()
if sum(score_player1) > sum(score_player2):
    layout = [[sg.Text("player1: " + str(sum(score_player1)) + "\t\t player2: " + str(sum(score_player2)))],
              [sg.Text("congratiolations player 1 wins")],
              [sg.Button("end", bind_return_key=False)]]
    window = sg.Window('game', layout)
if sum(score_player1) < sum(score_player2):
    layout = [[sg.Text("player1: " + str(sum(score_player1)) + "\t\t player2: " + str(sum(score_player2)))],
              [sg.Text("congratiolations player 2 wins")],
              [sg.Button("end", bind_return_key=False)]]
    window = sg.Window('game', layout)
if sum(score_player1) == sum(score_player2):
    layout = [[sg.Text("player1: " + str(sum(score_player1)) + "\t\t player2: " + str(sum(score_player2)))],
              [sg.Text("its a draw")],
              [sg.Button("end", bind_return_key=False)]]
    window = sg.Window('game', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "end":  # if user closes window or clicks cancel
        break
window.close()
