import PySimpleGUI as sg


from util_funcs import *

# functions to build screen


def new_screen(score_player1, score_player2, options_player1, options_player2, counter_player1, counter_player2, dice_player1, dice_player2, points_player1, points_player2, turn, tries):
    if turn == 0:
        pl1 = (show_points(score_player1, [
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], points_player1, dice_player1))
        pl2 = score_player2
        if tries <= 2:
            layout = [[sg.Text("player1", visible=True), (sg.Text("\t\t        player2", visible=True, key="name_2"))],
                      [(sg.Text("player 1 score: "+str(sum(score_player1)))),
                       (sg.Text("\t         player 2 score: "+str(sum(score_player2))))],
                      [(sg.Checkbox(dice_player1[0][0], visible=True, default=dice_player1[0][1], key="1")), (sg.Checkbox(dice_player1[1][0], visible=True, default=dice_player1[1][1], key="2")), (sg.Checkbox(dice_player1[2][0], visible=True, default=dice_player1[2][1], key="3")),
                       (sg.Checkbox(dice_player1[3][0], visible=True, default=dice_player1[3][1], key="4")), (sg.Checkbox(
                           dice_player1[4][0], visible=True, default=dice_player1[4][1], key="5")), sg.Text("\t\t              "),
                       (sg.Checkbox(dice_player2[0][0], visible=False, default=dice_player2[0][1], key="6")), (sg.Checkbox(
                           dice_player2[1][0], visible=False, default=dice_player2[1][1], key="7")), (sg.Checkbox(dice_player2[2][0], visible=False, default=dice_player2[2][1], key="8")),
                       (sg.Checkbox(dice_player2[3][0], visible=False, default=dice_player2[3][1], key="9")), sg.Checkbox(dice_player2[4][0], visible=False, default=dice_player2[4][1], key="10")],
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
                      [(sg.Checkbox(dice_player1[0][0], visible=True, default=dice_player1[0][1], key="1")), (sg.Checkbox(dice_player1[1][0], visible=True, default=dice_player1[1][1], key="2")), (sg.Checkbox(dice_player1[2][0], visible=True, default=dice_player1[2][1], key="3")),
                       (sg.Checkbox(dice_player1[3][0], visible=True, default=dice_player1[3][1], key="4")), (sg.Checkbox(
                           dice_player1[4][0], visible=True, default=dice_player1[4][1], key="5")), sg.Text("\t\t              "),
                       (sg.Checkbox(dice_player2[0][0], visible=False, default=dice_player2[0][1], key="6")), (sg.Checkbox(
                           dice_player2[1][0], visible=False, default=dice_player2[1][1], key="7")), (sg.Checkbox(dice_player2[2][0], visible=False, default=dice_player2[2][1], key="8")),
                       (sg.Checkbox(dice_player2[3][0], visible=False, default=dice_player2[3][1], key="9")), sg.Checkbox(dice_player2[4][0], visible=False, default=dice_player2[4][1], key="10")],
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
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], points_player2, dice_player2))
            layout = [[sg.Text("player1", visible=True), (sg.Text("\t\t        player2", visible=True, key="name_2"))],
                      [(sg.Text("player 1 score: "+str(sum(score_player1)))),
                       (sg.Text("\t         player 2 score: "+str(sum(score_player2))))],
                      [(sg.Checkbox(dice_player1[0][0], visible=False, default=dice_player1[0][1], key="1")), (sg.Checkbox(dice_player1[1][0], visible=False, default=dice_player1[1][1], key="2")), (sg.Checkbox(dice_player1[2][0], visible=False, default=dice_player1[2][1], key="3")),
                       (sg.Checkbox(dice_player1[3][0], visible=False, default=dice_player1[3][1], key="4")), (sg.Checkbox(
                           dice_player1[4][0], visible=False, default=dice_player1[4][1], key="5")), sg.Text("\t\t              "),
                       (sg.Checkbox(dice_player2[0][0], visible=True, default=dice_player2[0][1], key="6")), (sg.Checkbox(
                           dice_player2[1][0], visible=True, default=dice_player2[1][1], key="7")), (sg.Checkbox(dice_player2[2][0], visible=True, default=dice_player2[2][1], key="8")),
                       (sg.Checkbox(dice_player2[3][0], visible=True, default=dice_player2[3][1], key="9")), sg.Checkbox(dice_player2[4][0], visible=True, default=dice_player2[4][1], key="10")],
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
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], points_player2, dice_player2))
            layout = [[sg.Text("player1", visible=True), (sg.Text("\t\t        player2", visible=True, key="name_2"))],
                      [(sg.Text("player 1 score: "+str(sum(score_player1)))),
                       (sg.Text("\t         player 2 score: "+str(sum(score_player2))))],
                      [(sg.Checkbox(dice_player1[0][0], visible=False, default=dice_player1[0][1], key="1")), (sg.Checkbox(dice_player1[1][0], visible=False, default=dice_player1[1][1], key="2")), (sg.Checkbox(dice_player1[2][0], visible=False, default=dice_player1[2][1], key="3")),
                       (sg.Checkbox(dice_player1[3][0], visible=False, default=dice_player1[3][1], key="4")), (sg.Checkbox(
                           dice_player1[4][0], visible=False, default=dice_player1[4][1], key="5")), sg.Text("\t\t              "),
                       (sg.Checkbox(dice_player2[0][0], visible=True, default=dice_player2[0][1], key="6")), (sg.Checkbox(
                           dice_player2[1][0], visible=True, default=dice_player2[1][1], key="7")), (sg.Checkbox(dice_player2[2][0], visible=True, default=dice_player2[2][1], key="8")),
                       (sg.Checkbox(dice_player2[3][0], visible=True, default=dice_player2[3][1], key="9")), sg.Checkbox(dice_player2[4][0], visible=True, default=dice_player2[4][1], key="10")],
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
