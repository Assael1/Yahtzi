
from util_funcs import *
from ui import *
from logic import *

# game starts here
score_player1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
score_player2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 0
end = 0

options_player1 = ["1", "2", "3", "4", "5", "6", "x3", "x4",
                   "full house", "small", "big", "yatzy", "sum", "second yatzy"]
options_player2 = ["1", "2", "3", "4", "5", "6", "x3", "x4",
                   "full house", "small", "big", "yatzy", "sum", "second yatzy"]
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
    dice_player1 = [[random.randint(1, 6), False], [random.randint(1, 6), False], [
        random.randint(1, 6), False], [random.randint(1, 6), False], [random.randint(1, 6), False]]
    dice_player2 = [[random.randint(1, 6), False], [random.randint(1, 6), False], [
        random.randint(1, 6), False], [random.randint(1, 6), False], [random.randint(1, 6), False]]
    # if i==20:
    #      dice_player1=[[1,False],[2,False],[3,False],[4,False],[5,False]]
    points_player1 = [one(dice_player1), two(dice_player1), three(dice_player1), four(dice_player1), five(dice_player1), six(dice_player1), X3(dice_player1), X4(dice_player1), full_house(
        dice_player1), small(dice_player1), long(dice_player1), yatzy(dice_player1), sum(row[0] for row in dice_player1), bonus(score_player1, options_player1, options), yatzy(dice_player1)]
    points_player2 = [one(dice_player2), two(dice_player2), three(dice_player2), four(dice_player2), five(dice_player2), six(dice_player2), X3(dice_player2), X4(dice_player2), full_house(
        dice_player2), small(dice_player2), long(dice_player2), yatzy(dice_player2), sum(row[0] for row in dice_player2), bonus(score_player2, options_player2, options), yatzy(dice_player2)]
    layout = new_screen(score_player1, score_player2, options_player1, options_player2, counter_player1,
                        counter_player2, dice_player1, dice_player2, points_player1, points_player2, turn, tries)
    window = sg.Window('game', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break
        if event == "next":
            if turn == 0:
                window.close()
                play = common(dice_player1, options_player1)
                if end == 1:
                    play = common_to_end(dice_player1)
                    print(play)
                dice_player1 = choose_what_to_keep(
                    play, dice_player1, options_player1)
                dice_player1 = change_dice(
                    dice_player1, turn, window, tries)
                points_player1 = [one(dice_player1), two(dice_player1), three(dice_player1), four(dice_player1), five(dice_player1), six(dice_player1), X3(dice_player1), X4(dice_player1), full_house(
                    dice_player1), small(dice_player1), long(dice_player1), yatzy(dice_player1), sum(row[0] for row in dice_player1), bonus(score_player1, options_player1, options), yatzy(dice_player1)]
                points_player2 = [one(dice_player2), two(dice_player2), three(dice_player2), four(dice_player2), five(dice_player2), six(dice_player2), X3(dice_player2), X4(dice_player2), full_house(
                    dice_player2), small(dice_player2), long(dice_player2), yatzy(dice_player2), sum(row[0] for row in dice_player2), bonus(score_player2, options_player2, options), yatzy(dice_player2)]
                layout = new_screen(score_player1, score_player2, options_player1, options_player2, counter_player1,
                                    counter_player2, dice_player1, dice_player2, points_player1, points_player2, turn, tries)
                window = sg.Window('game', layout)
                while True:
                    event, values = window.read()
                    if event == "next":
                        window.close()
                        play = common(dice_player1, options_player1)
                        if end == 1:
                            play = common_to_end(dice_player1)
                            print(play)
                        dice_player1 = choose_what_to_keep(
                            play, dice_player1, options_player1)
                        dice_player1 = change_dice(
                            dice_player1, turn, window, tries)
                        points_player1 = [one(dice_player1), two(dice_player1), three(dice_player1), four(dice_player1), five(dice_player1), six(dice_player1), X3(dice_player1), X4(dice_player1), full_house(
                            dice_player1), small(dice_player1), long(dice_player1), yatzy(dice_player1), sum(row[0] for row in dice_player1), bonus(score_player1, options_player1, options), yatzy(dice_player1)]
                        points_player2 = [one(dice_player2), two(dice_player2), three(dice_player2), four(dice_player2), five(dice_player2), six(dice_player2), X3(dice_player2), X4(dice_player2), full_house(
                            dice_player2), small(dice_player2), long(dice_player2), yatzy(dice_player2), sum(row[0] for row in dice_player2), bonus(score_player2, options_player2, options), yatzy(dice_player2)]
                        layout = new_screen(score_player1, score_player2, options_player1, options_player2, counter_player1,
                                            counter_player2, dice_player1, dice_player2, points_player1, points_player2, turn, tries)
                        window = sg.Window('game', layout)
                        while True:
                            event, values = window.read()
                            if event == "next":
                                points_player1 = [one(dice_player1), two(dice_player1), three(dice_player1), four(dice_player1), five(dice_player1), six(dice_player1), X3(dice_player1), X4(dice_player1), full_house(
                                    dice_player1), small(dice_player1), long(dice_player1), yatzy(dice_player1), sum(row[0] for row in dice_player1), bonus(score_player1, options_player1, options), yatzy(dice_player1)]
                                com1, place1 = max_here(
                                    points_player1, options, options_player1)
                                for i in options[8:12]:
                                    if choose_special(dice_player1, options_player1, i, points_player1) != -1:
                                        flag = choose_special(
                                            dice_player1, options_player1, i, points_player1)
                                if score_player1[11] != 0:
                                    if choose_special(dice_player1, options_player1, "second yatzy", points_player1) != -1:
                                        flag = choose_special(
                                            dice_player1, options_player1, "second yatzy", points_player1)
                                if flag == -1:
                                    play = find(play, options_player1)
                                    if play == -1:
                                        end = 1
                                        com1, place1 = max_here(
                                            points_player1, options, options_player1)
                                        play = find(
                                            options[place1], options_player1)
                                    options_player1, options_player2, score_player1, score_player2 = ok_choose(
                                        turn, score_player1, score_player2, dice_player1, dice_player2, options_player1, options_player2, options_player1[play], options[place1])
                                else:
                                    options_player1, options_player2, score_player1, score_player2 = ok_choose(
                                        turn, score_player1, score_player2, dice_player1, dice_player2, options_player1, options_player2, options_player1[flag], options[place1])
                                break
                        break
                #com1, place1 = max_here(points_player1,options,options_player1)
                #options_player1, options_player2 , score_player1,score_player2 =ok_choose(turn,score_player1,score_player2,dice_player1,dice_player2,options_player1,options_player2,options[place1],options[play])
            if turn == 1:
                window.close()
                play = common(dice_player2, options_player2)
                if play == 1:
                    if count(dice_player2, play) == 4:
                        dice_player2 = choose_what_to_keep(
                            play, dice_player2, options_player2)
                        dice_player2 = change_dice(
                            dice_player2, turn, window, tries)
                    else:
                        dice_player2 = change_dice(
                            dice_player2, turn, window, tries)
                if 2 <= play <= 6:
                    #dice_player2 = keep_number(dice_player2,play)
                    dice_player2 = choose_what_to_keep(
                        play, dice_player2, options_player2)
                    dice_player2 = change_dice(
                        dice_player2, turn, window, tries)
                if play == -1:
                    play = temp
                    dice_player2 = choose_what_to_keep(
                        play, dice_player2, options_player2)
                    dice_player2 = change_dice(
                        dice_player2, turn, window, tries)
                points_player1 = [one(dice_player1), two(dice_player1), three(dice_player1), four(dice_player1), five(dice_player1), six(dice_player1), X3(dice_player1), X4(dice_player1), full_house(
                    dice_player1), small(dice_player1), long(dice_player1), yatzy(dice_player1), sum(row[0] for row in dice_player1), bonus(score_player1, options_player1, options), yatzy(dice_player1)]
                points_player2 = [one(dice_player2), two(dice_player2), three(dice_player2), four(dice_player2), five(dice_player2), six(dice_player2), X3(dice_player2), X4(dice_player2), full_house(
                    dice_player2), small(dice_player2), long(dice_player2), yatzy(dice_player2), sum(row[0] for row in dice_player2), bonus(score_player2, options_player2, options), yatzy(dice_player2)]
                layout = new_screen(score_player1, score_player2, options_player1, options_player2, counter_player1,
                                    counter_player2, dice_player1, dice_player2, points_player1, points_player2, turn, tries)
                window = sg.Window('game', layout)
                while True:
                    event, values = window.read()
                    if event == "next":
                        window.close()
                        play = common(dice_player2, options_player2)
                        if 2 <= play <= 6:
                            dice_player2 = choose_what_to_keep(
                                play, dice_player2, options_player2)
                            dice_player2 = change_dice(
                                dice_player2, turn, window, tries)
                        if play == -1:
                            play = temp
                            dice_player2 = choose_what_to_keep(
                                play, dice_player2, options_player2)
                            dice_player2 = change_dice(
                                dice_player2, turn, window, tries)
                        points_player1 = [one(dice_player1), two(dice_player1), three(dice_player1), four(dice_player1), five(dice_player1), six(dice_player1), X3(dice_player1), X4(dice_player1), full_house(
                            dice_player1), small(dice_player1), long(dice_player1), yatzy(dice_player1), sum(row[0] for row in dice_player1), bonus(score_player1, options_player1, options), yatzy(dice_player1)]
                        points_player2 = [one(dice_player2), two(dice_player2), three(dice_player2), four(dice_player2), five(dice_player2), six(dice_player2), X3(dice_player2), X4(dice_player2), full_house(
                            dice_player2), small(dice_player2), long(dice_player2), yatzy(dice_player2), sum(row[0] for row in dice_player2), bonus(score_player2, options_player2, options), yatzy(dice_player2)]
                        layout = new_screen(score_player1, score_player2, options_player1, options_player2, counter_player1,
                                            counter_player2, dice_player1, dice_player2, points_player1, points_player2, turn, tries)
                        window = sg.Window('game', layout)
                        while True:
                            event, values = window.read()
                            if event == "next":
                                points_player2 = [one(dice_player2), two(dice_player2), three(dice_player2), four(dice_player2), five(dice_player2), six(dice_player2), X3(dice_player2), X4(dice_player2), full_house(
                                    dice_player2), small(dice_player2), long(dice_player2), yatzy(dice_player2), sum(row[0] for row in dice_player2), bonus(score_player2, options_player2, options), yatzy(dice_player2)]
                                com2, place2 = max_here(
                                    points_player2, options, options_player2)
                                options_player1, options_player2, score_player1, score_player2 = ok_choose(
                                    turn, score_player1, score_player2, dice_player1, dice_player2, options_player1, options_player2, options[place2], options[place2])
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
