# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 09:53:49 2022

@author: nir
"""

import random
import PySimpleGUI as sg
import pickle

#functions for points
def one (dices):
    count = 0
    for i in dices:
        if i[0] ==1:
            count +=1
    return count
def two (dices):
    count = 0
    for i in dices:
        if i[0] ==2:
            count +=1
    return count*2
def three (dices):
    count = 0
    for i in dices:
        if i[0] ==3:
            count +=1
    return count*3
def four (dices):
    count = 0
    for i in dices:
        if i[0] ==4:
            count +=1
    return count*4
def five (dices):
    count = 0
    for i in dices:
        if i[0] ==5:
            count +=1
    return count*5
def six (dices):
    count = 0
    for i in dices:
        if i[0] ==6:
            count +=1
    return count*6
def X3 (dices):
    dices0=list (dices)
    dices0.sort()
    if dices0[0][0]==dices0[1][0]==dices0[2][0] or dices0[2][0]==dices0[3][0]==dices0[4][0]:
        return sum(row[0] for row in dices)
    return 0
def X4 (dices):
    dices0=list (dices)
    dices0.sort()
    if dices0[0][0]==dices0[1][0]==dices0[2][0]==dices0[3][0] or dices0[1][0]==dices0[2][0]==dices0[3][0]==dices0[4][0]:
        return sum(row[0] for row in dices)
    return 0
def full_house (dices):
    dices0=list (dices)
    dices0.sort()
    if dices0[0][0]==dices0[1][0]==dices0[2][0] and dices0[2][0]!=dices0[3][0]==dices0[4][0]:
        return 25
    if dices0[0][0]==dices0[1][0]!=dices0[2][0] and dices0[2][0]==dices0[3][0]==dices0[4][0]:
        return 25
    return 0
def small (dices):
    dices0=list (dices)
    dices0.sort()
    if dices0[4][0]==dices0[3][0]+1==dices0[2][0]+2==dices0[1][0]+3 or dices0[3][0]==dices0[2][0]+1==dices0[1][0]+2==dices0[0][0]+3:
        return 30
    if dices0[3][0]==dices0[2][0]:
        if dices0[4][0]==dices0[2][0]+1==dices0[1][0]+2==dices0[0][0]+3:
            return 30
    if dices0[2][0]==dices0[1][0]:
        if dices0[4][0]==dices0[3][0]+1==dices0[1][0]+2==dices0[0][0]+3:
            return 30
    return 0
def long (dices):
    dices0=list (dices)
    dices0.sort()
    if dices0[4][0]==dices0[3][0]+1==dices0[2][0]+2==dices0[1][0]+3==dices0[0][0]+4:
        return 40
    return 0
def yatzy(dices):
    if dices[0][0]==dices[1][0]==dices[2][0]==dices[3][0]==dices[4][0]:
        return 50
    return 0
def check_for_bonus(score):
    if sum(score[0:6])>63:
        score[13]=35
    return score
def show_points(score,temp,points,dices):
    for i in range(len(score)):
        if score[i] != 0:
            temp[i] = score[i]
        if score[i] == 0:
            temp[i] = "[" + str(points[i]) + "]"
    return temp
def bonus(score,options_player,options):
    counter =0
    for i in range(6):
        if options[i] is not options_player:
            counter += -3*(i+1)+score[i]
    return counter
def change_dices(dices,turn,window,round):
        if turn ==0:
            if values["1"]==False:
                dices[0][0]= random.randint(1,6)
            else:
                dices[0][1]=True
            if values["2"]==False:
                dices[1][0]= random.randint(1,6)
            else:
                dices[1][1]=True
            if values["3"]==False:
                dices[2][0]= random.randint(1,6)
            else:
                dices[2][1]=True
            if values["4"]==False:
                dices[3][0]= random.randint(1,6)
            else:
                dices[3][1]=True
            if values["5"]==False:
                dices[4][0]= random.randint(1,6)
            else:
                dices[4][1]=True
        if turn == 1:
            if values["6"]==False:
                dices[0][0]= random.randint(1,6)
            else:
                dices[0][1]=True
            if values["7"]==False:
                dices[1][0]= random.randint(1,6)
            else:
                dices[1][1]=True
            if values["8"]==False:
                dices[2][0]= random.randint(1,6)
            else:
                dices[2][1]=True
            if values["9"]==False:
                dices[3][0]= random.randint(1,6)
            else:
                dices[3][1]=True
            if values["10"]==False:
                dices[4][0]= random.randint(1,6)
            else:
                dices[4][1]=True
        return dices
def new_screen(score_player1,score_player2,options_player1,options_player2,counter_player1,counter_player2,dices_player1,dices_player2,points_player1,points_player2,turn,tries):
    if turn ==0:
        pl1=(show_points(score_player1, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], points_player1, dices_player1))
        pl2=score_player2
        if tries <=2:
            layout = [[sg.Text("player1",visible=True),(sg.Text("\t\t        player2",visible=True,key="name_2"))],
                      [(sg.Text("player 1 score: "+str (sum(score_player1)))),(sg.Text("\t         player 2 score: "+str (sum(score_player2))))],
                      [(sg.Checkbox(dices_player1[0][0],visible=True,default =dices_player1[0][1] ,key = "1")),(sg.Checkbox(dices_player1[1][0],visible=True,default =dices_player1[1][1],key = "2")),(sg.Checkbox(dices_player1[2][0],visible=True,default =dices_player1[2][1],key = "3")),
                       (sg.Checkbox(dices_player1[3][0],visible=True,default =dices_player1[3][1],key = "4")),(sg.Checkbox(dices_player1[4][0],visible=True,default =dices_player1[4][1],key = "5")),sg.Text("\t\t              "),
                       (sg.Checkbox(dices_player2[0][0],visible=False,default =dices_player2[0][1],key = "6")),(sg.Checkbox(dices_player2[1][0],visible=False,default =dices_player2[1][1],key = "7")),(sg.Checkbox(dices_player2[2][0],visible=False,default =dices_player2[2][1],key = "8")),
                       (sg.Checkbox(dices_player2[3][0],visible=False,default =dices_player2[3][1],key = "9")),sg.Checkbox(dices_player2[4][0],visible=False,default =dices_player2[4][1],key = "10")],
                      [(sg.Text("1: " + str (pl1[0]),key="a1")),(sg.Text("  X3: " +str(pl1[6]),key="a2")),(sg.Text("       \t          1: " + str (pl2[0]),key="b1")),(sg.Text("  X3: " +str(pl2[6]),key="b2"))],
                      [(sg.Text("2: "+str(pl1[1]),key="a3")),(sg.Text("  X4: " + str (pl1[7]),key="a4")),(sg.Text("           \t          2: "+str(pl2[1]),key="b3")),(sg.Text("  X4: " + str (pl2[7]),key="b4"))],
                      [(sg.Text("3: " + str(pl1[2]),key="a5")),(sg.Text("  full house: " + str (pl1[8]),key="a6")),(sg.Text("        \t3: " + str(pl2[2]),key="b5")),(sg.Text("  full house: " + str (pl2[8]),key="b6"))],
                      [(sg.Text("4: " + str(pl1[3]),key="a7")),(sg.Text("  small straight: " + str (pl1[9]),key="a8")),(sg.Text("        4: " + str(pl2[3]),key="b7")),(sg.Text("  small straight: " + str (pl2[9]),key="b8"))],
                      [(sg.Text("5: " +str(pl1[4]),key="a9")),(sg.Text("  big sraight: " + str(pl1[10]),key="a10")),(sg.Text("            5: " + str(pl2[4]),key="b9")),(sg.Text("  big sraight: " + str (pl2[10]),key="b10"))],
                      [(sg.Text("6: " +str (pl1[5]),key="a11")),(sg.Text("  yatzy: " + str (pl1[11]),key="a12")),(sg.Text("\t      6: " + str(pl2[5]),key="b11")),(sg.Text("  yatzy: " + str (pl2[11]),key="b12"))],
                      [(sg.Text("sum: " + str (pl1[12]),key="a13")),sg.Text("second yatzy: " + str (pl1[14]),key="a14"),(sg.Text("     sum: " + str (pl2[12]),key="b13")),sg.Text("second yatzy: " + str (pl1[14]),key="b14")],
                      [sg.Text("bonus under\over: " + str(pl1[13])),sg.Text("         "),sg.Text("bonus under\over: " + str(pl2[13]))],
                      [sg.OptionMenu(options_player1,visible=True,text_color="white",background_color="blue",key="choose1"),sg.Text("\t\t             "),(sg.OptionMenu(options_player2,visible=False,text_color="white",background_color="blue",key="choose2"))],
                      [(sg.Text("\t\t    ")),(sg.Button("ok")),(sg.Button("roll"))]]
            return layout
        else:
            layout = [[sg.Text("player1",visible=True),(sg.Text("\t\t        player2",visible=True,key="name_2"))],
                      [(sg.Text("player 1 score: "+str (sum(score_player1)))),(sg.Text("\t         player 2 score: "+str (sum(score_player2))))],
                      [(sg.Checkbox(dices_player1[0][0],visible=True,default =dices_player1[0][1] ,key = "1")),(sg.Checkbox(dices_player1[1][0],visible=True,default =dices_player1[1][1],key = "2")),(sg.Checkbox(dices_player1[2][0],visible=True,default =dices_player1[2][1],key = "3")),
                       (sg.Checkbox(dices_player1[3][0],visible=True,default =dices_player1[3][1],key = "4")),(sg.Checkbox(dices_player1[4][0],visible=True,default =dices_player1[4][1],key = "5")),sg.Text("\t\t              "),
                       (sg.Checkbox(dices_player2[0][0],visible=False,default =dices_player2[0][1],key = "6")),(sg.Checkbox(dices_player2[1][0],visible=False,default =dices_player2[1][1],key = "7")),(sg.Checkbox(dices_player2[2][0],visible=False,default =dices_player2[2][1],key = "8")),
                       (sg.Checkbox(dices_player2[3][0],visible=False,default =dices_player2[3][1],key = "9")),sg.Checkbox(dices_player2[4][0],visible=False,default =dices_player2[4][1],key = "10")],
                      [(sg.Text("1: " + str (pl1[0]),key="a1")),(sg.Text("  X3: " +str(pl1[6]),key="a2")),(sg.Text("       \t          1: " + str (pl2[0]),key="b1")),(sg.Text("  X3: " +str(pl2[6]),key="b2"))],
                      [(sg.Text("2: "+str(pl1[1]),key="a3")),(sg.Text("  X4: " + str (pl1[7]),key="a4")),(sg.Text("           \t          2: "+str(pl2[1]),key="b3")),(sg.Text("  X4: " + str (pl2[7]),key="b4"))],
                      [(sg.Text("3: " + str(pl1[2]),key="a5")),(sg.Text("  full house: " + str (pl1[8]),key="a6")),(sg.Text("        \t3: " + str(pl2[2]),key="b5")),(sg.Text("  full house: " + str (pl2[8]),key="b6"))],
                      [(sg.Text("4: " + str(pl1[3]),key="a7")),(sg.Text("  small straight: " + str (pl1[9]),key="a8")),(sg.Text("        4: " + str(pl2[3]),key="b7")),(sg.Text("  small straight: " + str (pl2[9]),key="b8"))],
                      [(sg.Text("5: " +str(pl1[4]),key="a9")),(sg.Text("  big sraight: " + str(pl1[10]),key="a10")),(sg.Text("            5: " + str(pl2[4]),key="b9")),(sg.Text("  big sraight: " + str (pl2[10]),key="b10"))],
                      [(sg.Text("6: " +str (pl1[5]),key="a11")),(sg.Text("  yatzy: " + str (pl1[11]),key="a12")),(sg.Text("\t      6: " + str(pl2[5]),key="b11")),(sg.Text("  yatzy: " + str (pl2[11]),key="b12"))],
                      [(sg.Text("sum: " + str (pl1[12]),key="a13")),sg.Text("second yatzy: " + str (pl1[14]),key="a14"),(sg.Text("     sum: " + str (pl2[12]),key="b13")),sg.Text("second yatzy: " + str (pl1[14]),key="b14")],
                      [sg.Text("bonus under\over: " + str(pl1[13])),sg.Text("         "),sg.Text("bonus under\over: " + str(pl2[13]))],
                      [sg.OptionMenu(options_player1,visible=True,text_color="white",background_color="blue",key="choose1"),sg.Text("\t\t             "),(sg.OptionMenu(options_player2,visible=False,text_color="white",background_color="blue",key="choose2"))],
                      [(sg.Text("\t\t    ")),(sg.Button("ok"))]]
            return layout
    if turn ==1:
        if tries <=2:
            pl1 = score_player1
            pl2=(show_points(score_player2, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], points_player2, dices_player2))
            layout = [[sg.Text("player1",visible=True),(sg.Text("\t\t        player2",visible=True,key="name_2"))],
                          [(sg.Text("player 1 score: "+str (sum(score_player1)))),(sg.Text("\t         player 2 score: "+str (sum(score_player2))))],
                      [(sg.Checkbox(dices_player1[0][0],visible=False,default =dices_player1[0][1] ,key = "1")),(sg.Checkbox(dices_player1[1][0],visible=False,default =dices_player1[1][1],key = "2")),(sg.Checkbox(dices_player1[2][0],visible=False,default =dices_player1[2][1],key = "3")),
                       (sg.Checkbox(dices_player1[3][0],visible=False,default =dices_player1[3][1],key = "4")),(sg.Checkbox(dices_player1[4][0],visible=False,default =dices_player1[4][1],key = "5")),sg.Text("\t\t              "),
                       (sg.Checkbox(dices_player2[0][0],visible=True,default =dices_player2[0][1],key = "6")),(sg.Checkbox(dices_player2[1][0],visible=True,default =dices_player2[1][1],key = "7")),(sg.Checkbox(dices_player2[2][0],visible=True,default =dices_player2[2][1],key = "8")),
                       (sg.Checkbox(dices_player2[3][0],visible=True,default =dices_player2[3][1],key = "9")),sg.Checkbox(dices_player2[4][0],visible=True,default =dices_player2[4][1],key = "10")],
                      [(sg.Text("1: " + str (pl1[0]),key="a1")),(sg.Text("  X3: " +str(pl1[6]),key="a2")),(sg.Text("       \t          1: " + str (pl2[0]),key="b1")),(sg.Text("  X3: " +str(pl2[6]),key="b2"))],
                      [(sg.Text("2: "+str(pl1[1]),key="a3")),(sg.Text("  X4: " + str (pl1[7]),key="a4")),(sg.Text("           \t          2: "+str(pl2[1]),key="b3")),(sg.Text("  X4: " + str (pl2[7]),key="b4"))],
                      [(sg.Text("3: " + str(pl1[2]),key="a5")),(sg.Text("  full house: " + str (pl1[8]),key="a6")),(sg.Text("        \t3: " + str(pl2[2]),key="b5")),(sg.Text("  full house: " + str (pl2[8]),key="b6"))],
                      [(sg.Text("4: " + str(pl1[3]),key="a7")),(sg.Text("  small straight: " + str (pl1[9]),key="a8")),(sg.Text("        4: " + str(pl2[3]),key="b7")),(sg.Text("  small straight: " + str (pl2[9]),key="b8"))],
                      [(sg.Text("5: " +str(pl1[4]),key="a9")),(sg.Text("  big sraight: " + str(pl1[10]),key="a10")),(sg.Text("            5: " + str(pl2[4]),key="b9")),(sg.Text("  big sraight: " + str (pl2[10]),key="b10"))],
                      [(sg.Text("6: " +str (pl1[5]),key="a11")),(sg.Text("  yatzy: " + str (pl1[11]),key="a12")),(sg.Text("\t      6: " + str(pl2[5]),key="b11")),(sg.Text("  yatzy: " + str (pl2[11]),key="b12"))],
                      [(sg.Text("sum: " + str (pl1[12]),key="a13")),sg.Text("second yatzy: " + str (pl1[14]),key="a14"),(sg.Text("     sum: " + str (pl2[12]),key="b13")),sg.Text("second yatzy: " + str (pl1[14]),key="b14")],
                      [sg.Text("bonus under\over: " + str(pl1[13])),sg.Text("         "),sg.Text("bonus under\over: " + str(pl2[13]))],
                      [sg.OptionMenu(options_player1,visible=False,text_color="white",background_color="blue",key="choose1"),sg.Text("\t\t             "),(sg.OptionMenu(options_player2,visible=True,text_color="white",background_color="blue",key="choose2"))],
                      [(sg.Text("\t\t    ")),(sg.Button("ok")),(sg.Button("roll"))]]
            return layout
        else:
            pl1 = score_player1
            pl2=(show_points(score_player2, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], points_player2, dices_player2))
            layout = [[sg.Text("player1",visible=True),(sg.Text("\t\t        player2",visible=True,key="name_2"))],
                          [(sg.Text("player 1 score: "+str (sum(score_player1)))),(sg.Text("\t         player 2 score: "+str (sum(score_player2))))],
                      [(sg.Checkbox(dices_player1[0][0],visible=False,default =dices_player1[0][1] ,key = "1")),(sg.Checkbox(dices_player1[1][0],visible=False,default =dices_player1[1][1],key = "2")),(sg.Checkbox(dices_player1[2][0],visible=False,default =dices_player1[2][1],key = "3")),
                       (sg.Checkbox(dices_player1[3][0],visible=False,default =dices_player1[3][1],key = "4")),(sg.Checkbox(dices_player1[4][0],visible=False,default =dices_player1[4][1],key = "5")),sg.Text("\t\t              "),
                       (sg.Checkbox(dices_player2[0][0],visible=True,default =dices_player2[0][1],key = "6")),(sg.Checkbox(dices_player2[1][0],visible=True,default =dices_player2[1][1],key = "7")),(sg.Checkbox(dices_player2[2][0],visible=True,default =dices_player2[2][1],key = "8")),
                       (sg.Checkbox(dices_player2[3][0],visible=True,default =dices_player2[3][1],key = "9")),sg.Checkbox(dices_player2[4][0],visible=True,default =dices_player2[4][1],key = "10")],
                      [(sg.Text("1: " + str (pl1[0]),key="a1")),(sg.Text("  X3: " +str(pl1[6]),key="a2")),(sg.Text("       \t          1: " + str (pl2[0]),key="b1")),(sg.Text("  X3: " +str(pl2[6]),key="b2"))],
                      [(sg.Text("2: "+str(pl1[1]),key="a3")),(sg.Text("  X4: " + str (pl1[7]),key="a4")),(sg.Text("           \t          2: "+str(pl2[1]),key="b3")),(sg.Text("  X4: " + str (pl2[7]),key="b4"))],
                      [(sg.Text("3: " + str(pl1[2]),key="a5")),(sg.Text("  full house: " + str (pl1[8]),key="a6")),(sg.Text("        \t3: " + str(pl2[2]),key="b5")),(sg.Text("  full house: " + str (pl2[8]),key="b6"))],
                      [(sg.Text("4: " + str(pl1[3]),key="a7")),(sg.Text("  small straight: " + str (pl1[9]),key="a8")),(sg.Text("        4: " + str(pl2[3]),key="b7")),(sg.Text("  small straight: " + str (pl2[9]),key="b8"))],
                      [(sg.Text("5: " +str(pl1[4]),key="a9")),(sg.Text("  big sraight: " + str(pl1[10]),key="a10")),(sg.Text("            5: " + str(pl2[4]),key="b9")),(sg.Text("  big sraight: " + str (pl2[10]),key="b10"))],
                      [(sg.Text("6: " +str (pl1[5]),key="a11")),(sg.Text("  yatzy: " + str (pl1[11]),key="a12")),(sg.Text("\t      6: " + str(pl2[5]),key="b11")),(sg.Text("  yatzy: " + str (pl2[11]),key="b12"))],
                      [(sg.Text("sum: " + str (pl1[12]),key="a13")),sg.Text("second yatzy: " + str (pl1[14]),key="a14"),(sg.Text("     sum: " + str (pl2[12]),key="b13")),sg.Text("second yatzy: " + str (pl1[14]),key="b14")],
                      [sg.Text("bonus under\over: " + str(pl1[13])),sg.Text("         "),sg.Text("bonus under\over: " + str(pl2[13]))],
                      [sg.OptionMenu(options_player1,visible=False,text_color="white",background_color="blue",key="choose1"),sg.Text("\t\t             "),(sg.OptionMenu(options_player2,visible=True,text_color="white",background_color="blue",key="choose2"))],
                      [(sg.Text("\t\t    ")),(sg.Button("ok"))]]
            return layout
def ok_choose(turn,score_player1,score_player2,dices_player1,dices_player2,options_player1,options_player2,values):
        if turn == 0:
            if values["choose1"]=="1":
                score_player1[0]=one(dices_player1)
                options_player1.remove("1")
            if values["choose1"]=="2":
                score_player1[1]=two(dices_player1)
                options_player1.remove("2")
            if values["choose1"]=="3":
                score_player1[2]=three(dices_player1)
                options_player1.remove("3")
            if values["choose1"]=="4":
                score_player1[3]=four(dices_player1)
                options_player1.remove("4")
            if values["choose1"]=="5":
                score_player1[4]=five(dices_player1)
                options_player1.remove("5")
            if values["choose1"]=="6":
                score_player1[5]=six(dices_player1)
                options_player1.remove("6")
            if values["choose1"]=="x3":
                score_player1[6]=X3(dices_player1)
                options_player1.remove("x3")
            if values["choose1"]=="x4":
                score_player1[7]=X4(dices_player1)
                options_player1.remove("x4")
            if values["choose1"]=="full house":
                score_player1[8]=full_house(dices_player1)
                options_player1.remove("full house")
            if values["choose1"]=="small":
                score_player1[9]=small(dices_player1)
                options_player1.remove("small")
            if values["choose1"]=="big":
                score_player1[10]=long(dices_player1)
                options_player1.remove("big")
            if values["choose1"]=="yatzy":
                score_player1[11]=yatzy(dices_player1)
                options_player1.remove("yatzy")
            if values["choose1"]=="sum":
                score_player1[12]=sum(dices_player1)
                options_player1.remove("sum")
            if values["choose1"]=="second yatzy":
                if score_player1!=0:
                    score_player1[14] = yatzy(dices_player1)
                options_player1.remove("second yatzy")
        else:
            if values["choose2"]=="1":
                score_player2[0]=one(dices_player2)
                options_player2.remove("1")
            if values["choose2"]=="2":
                score_player2[1]=two(dices_player2)
                options_player2.remove("2")
            if values["choose2"]=="3":
                score_player2[2]=three(dices_player2)
                options_player2.remove("3")
            if values["choose2"]=="4":
                score_player2[3]=four(dices_player2)
                options_player2.remove("4")
            if values["choose2"]=="5":
                score_player2[4]=five(dices_player2)
                options_player2.remove("5")
            if values["choose2"]=="6":
                score_player2[5]=six(dices_player2)
                options_player2.remove("6")
            if values["choose2"]=="x3":
                score_player2[6]=X3(dices_player2)
                options_player2.remove("x3")
            if values["choose2"]=="x4":
                score_player2[7]=X4(dices_player2)
                options_player2.remove("x4")
            if values["choose2"]=="full house":
                score_player2[8]=full_house(dices_player2)
                options_player2.remove("full house")
            if values["choose2"]=="small":
                score_player2[9]=small(dices_player2)
                options_player2.remove("small")
            if values["choose2"]=="big":
                score_player2[10]=long(dices_player2)
                options_player2.remove("big")
            if values["choose2"]=="yatzy":
                score_player2[11]=yatzy(dices_player2)
                options_player2.remove("yatzy")
            if values["choose2"]=="sum":
                score_player2[12]=sum(dices_player2)
                options_player2.remove("sum")
            if values["choose1"]=="second yatzy":
                if score_player2!=0:
                    score_player2[14] = yatzy(dices_player2)
                options_player2.remove("second yatzy")
        return options_player1, options_player2 , score_player1,score_player2 
## game starts here
score_player1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
score_player2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
turn = 0
options = ["1","2","3","4","5","6","x3","x4","full house","small","big","yatzy","sum","second yatzy"]
options_player1 = ["1","2","3","4","5","6","x3","x4","full house","small","big","yatzy","sum","second yatzy"]
options_player2 = ["1","2","3","4","5","6","x3","x4","full house","small","big","yatzy","sum","second yatzy"]
counter_player1 = sum(score_player1[0:6])
counter_player2 = sum(score_player2[0:6])
tries=1

sg.SetOptions(element_padding=(5,9),font=('Verdana',14),input_elements_background_color='#27F727',input_text_color='#ffffff') # Add a touch of color
for i in range(27):
    dices_player1 = [[random.randint(1,6),False],[random.randint(1,6),False],[random.randint(1,6),False],[random.randint(1,6),False],[random.randint(1,6),False]]
    dices_player2 = [[random.randint(1,6),False],[random.randint(1,6),False],[random.randint(1,6),False],[random.randint(1,6),False],[random.randint(1,6),False]]
    points_player1 = [one(dices_player1),two(dices_player1),three(dices_player1),four(dices_player1),five(dices_player1),six(dices_player1),X3(dices_player1),X4(dices_player1),full_house(dices_player1),small(dices_player1),long(dices_player1),yatzy(dices_player1),sum(row[0] for row in dices_player1),bonus(score_player1,options_player1,options),yatzy(dices_player1)]
    points_player2 = [one(dices_player2),two(dices_player2),three(dices_player2),four(dices_player2),five(dices_player2),six(dices_player2),X3(dices_player2),X4(dices_player2),full_house(dices_player2),small(dices_player2),long(dices_player2),yatzy(dices_player2),sum(row[0] for row in dices_player2),bonus(score_player2,options_player2,options),yatzy(dices_player2)]
    layout = new_screen(score_player1, score_player2, options_player1, options_player2, counter_player1, counter_player2, dices_player1, dices_player2, points_player1, points_player2, turn, tries)
    window = sg.Window('game',layout)
            # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break
        if event == "ok":
            tries=1
            options_player1, options_player2 , score_player1,score_player2 =ok_choose(turn,score_player1,score_player2,dices_player1,dices_player2,options_player1,options_player2,values)
            turn =(turn + 1)%2
            break
        if event == "roll":
            tries +=1
            window.close()
            if turn==0:
                dices_player1 = change_dices(dices_player1,turn,window,tries)
                points_player1 = [one(dices_player1),two(dices_player1),three(dices_player1),four(dices_player1),five(dices_player1),six(dices_player1),X3(dices_player1),X4(dices_player1),full_house(dices_player1),small(dices_player1),long(dices_player1),yatzy(dices_player1),sum(row[0] for row in dices_player1),bonus(score_player1,options_player1,options),yatzy(dices_player1)]
                points_player2 = [one(dices_player2),two(dices_player2),three(dices_player2),four(dices_player2),five(dices_player2),six(dices_player2),X3(dices_player2),X4(dices_player2),full_house(dices_player2),small(dices_player2),long(dices_player2),yatzy(dices_player2),sum(row[0] for row in dices_player2),bonus(score_player2,options_player2,options),yatzy(dices_player2)]
                layout = new_screen(score_player1, score_player2, options_player1, options_player2, counter_player1, counter_player2, dices_player1, dices_player2, points_player1, points_player2, turn, tries)
            if turn==1:
                dices_player2 = change_dices(dices_player2,turn,window,tries)
                points_player1 = [one(dices_player1),two(dices_player1),three(dices_player1),four(dices_player1),five(dices_player1),six(dices_player1),X3(dices_player1),X4(dices_player1),full_house(dices_player1),small(dices_player1),long(dices_player1),yatzy(dices_player1),sum(row[0] for row in dices_player1),bonus(score_player1,options_player1,options),yatzy(dices_player1)]
                points_player2 = [one(dices_player2),two(dices_player2),three(dices_player2),four(dices_player2),five(dices_player2),six(dices_player2),X3(dices_player2),X4(dices_player2),full_house(dices_player2),small(dices_player2),long(dices_player2),yatzy(dices_player2),sum(row[0] for row in dices_player2),bonus(score_player2,options_player2,options),yatzy(dices_player2)]
                layout = new_screen(score_player1, score_player2, options_player1, options_player2, counter_player1, counter_player2, dices_player1, dices_player2, points_player1, points_player2, turn, tries)
            window = sg.Window('game',layout)
            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
                    break
                if event == "ok":
                    tries=1
                    options_player1, options_player2 , score_player1,score_player2 =ok_choose(turn,score_player1,score_player2,dices_player1,dices_player2,options_player1,options_player2,values)
                    turn =(turn + 1)%2
                    break
                if event =="roll":
                    tries +=1
                    window.close()
                    if turn==0:
                        dices_player1 = change_dices(dices_player1,turn,window,tries)
                        points_player1 = [one(dices_player1),two(dices_player1),three(dices_player1),four(dices_player1),five(dices_player1),six(dices_player1),X3(dices_player1),X4(dices_player1),full_house(dices_player1),small(dices_player1),long(dices_player1),yatzy(dices_player1),sum(row[0] for row in dices_player1),bonus(score_player1,options_player1,options),yatzy(dices_player1)]
                        points_player2 = [one(dices_player2),two(dices_player2),three(dices_player2),four(dices_player2),five(dices_player2),six(dices_player2),X3(dices_player2),X4(dices_player2),full_house(dices_player2),small(dices_player2),long(dices_player2),yatzy(dices_player2),sum(row[0] for row in dices_player2),bonus(score_player2,options_player2,options),yatzy(dices_player2)]
                        layout = new_screen(score_player1, score_player2, options_player1, options_player2, counter_player1, counter_player2, dices_player1, dices_player2, points_player1, points_player2, turn, tries)
                    if turn==1:
                        dices_player2 = change_dices(dices_player2,turn,window,tries)
                        points_player1 = [one(dices_player1),two(dices_player1),three(dices_player1),four(dices_player1),five(dices_player1),six(dices_player1),X3(dices_player1),X4(dices_player1),full_house(dices_player1),small(dices_player1),long(dices_player1),yatzy(dices_player1),sum(row[0] for row in dices_player1),bonus(score_player1,options_player1,options),yatzy(dices_player1)]
                        points_player2 = [one(dices_player2),two(dices_player2),three(dices_player2),four(dices_player2),five(dices_player2),six(dices_player2),X3(dices_player2),X4(dices_player2),full_house(dices_player2),small(dices_player2),long(dices_player2),yatzy(dices_player2),sum(row[0] for row in dices_player2),bonus(score_player2,options_player2,options),yatzy(dices_player2)]
                        layout = new_screen(score_player1, score_player2, options_player1, options_player2, counter_player1, counter_player2, dices_player1, dices_player2, points_player1, points_player2, turn, tries)
                    window = sg.Window('game',layout)
                    while True:
                        event, values = window.read()
                        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
                            break
                        if event == "ok":
                            tries=1
                            options_player1, options_player2 , score_player1,score_player2 =ok_choose(turn,score_player1,score_player2,dices_player1,dices_player2,options_player1,options_player2,values)
                            turn =(turn + 1)%2
                            break
                break
        break
    counter_player1 = sum(score_player1[0:6])
    print(counter_player1)
    counter_player2 = sum(score_player2[0:6])
    if counter_player1>=63:
        score_player1[13]=35
    if counter_player2>=63:
        score_player2[13]=35
    window.close()
if sum(score_player1)>sum(score_player2):
    layout = [[ sg.Text("congratiolations player 1 wins")],
              [sg.Button("end")]]
    window = sg.Window('game',layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED  or event == "end": # if user closes window or clicks cancel
            break
window.close()