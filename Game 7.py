import tkinter
import numpy as np
import random
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk

root = Tk()
root.title("trajectory")
root.geometry("1600x1600")

root2 = Tk()
root2.title("results")
root2.geometry("1600x1600")



class GameSetUp:
    def __init__(self, master1, master2):
        self.myFrame = Frame(master1)
        self.myFrame.pack()
        self.myFrame2 = Frame(master2)
        self.myFrame2.pack()
        GameSetUp.datasetup(self)

        # create the text widget
        # text = tk.Text(root, height=10)
        # text.grid(row=0, column=0, sticky=tk.EW)

        # self.scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
        # self.scrollbar.grid(row=0, column=1, sticky=tk.NS)

    def determineGameOrder(self):
        self.numberofgames = int(3)
        UpperProb_game1 = 1 / self.numberofgames
        UpperProb_game2 = 2 / self.numberofgames

        # select the first item from the Game List

        ListofGame = [1, 2, 3]
        OrderedList = []

        randomGameSelector = random.random()
        if randomGameSelector > UpperProb_game2:
            Game = ListofGame[2]
        elif randomGameSelector > UpperProb_game1:
            Game = ListofGame[1]
        else:
            Game = ListofGame[0]

        ListofGame.remove(Game)
        OrderedList.append((Game))

        # select the second item from the Game List

        self.numberofgames = int(2)

        UpperProb_game1 = 1 / self.numberofgames

        randomGameSelector = random.random()
        if randomGameSelector > UpperProb_game1:
            Game = ListofGame[1]
        else:
            Game = ListofGame[0]

        ListofGame.remove(Game)
        OrderedList.append((Game))

        OrderedList.append(ListofGame[0])

        return OrderedList

    def updateGameMatricesBasedOnPreviousGame(self, game_played, game_affected, additional_cost):

        if game_played == 1 and game_affected ==2:
            change_to_game2 = float(self.TotalGameCostCorrelation_1_to_2.get())
            self.A2_active[0, 0] = self.A2_active[0,0] +  float(additional_cost) * change_to_game2
            self.A2_active[0, 1] = self.A2_active[0, 1] + float(additional_cost) * change_to_game2
            self.A2_active[1, 0] = self.A2_active[1, 0] + float(additional_cost) * change_to_game2
            self.A2_active[1, 1] = self.A2_active[1, 1] + float(additional_cost) * change_to_game2

            self.B2_active[0, 0] = self.B2_active[0, 0] + float(additional_cost) * change_to_game2
            self.B2_active[0, 1] = self.B2_active[0, 1] + float(additional_cost) * change_to_game2
            self.B2_active[1, 0] = self.B2_active[1, 0] + float(additional_cost) * change_to_game2
            self.B2_active[1, 1] = self.B2_active[1, 1] + float(additional_cost) * change_to_game2

        if game_played == 1 and game_affected == 3:
            change_to_game3 = float(self.TotalGameCostCorrelation_1_to_3.get())
            self.A3_active[0, 0] = self.A3_active[0,0] +  float(additional_cost) * change_to_game3
            self.A3_active[0, 1] = self.A3_active[0, 1] + float(additional_cost) * change_to_game3
            self.A3_active[1, 0] = self.A3_active[1, 0] + float(additional_cost) * change_to_game3
            self.A3_active[1, 1] = self.A3_active[1, 1] + float(additional_cost) * change_to_game3

            self.B3_active[0, 0] = self.B3_active[0, 0] + float(additional_cost) * change_to_game3
            self.B3_active[0, 1] = self.B3_active[0, 1] + float(additional_cost) * change_to_game3
            self.B3_active[1, 0] = self.B3_active[1, 0] + float(additional_cost) * change_to_game3
            self.B3_active[1, 1] = self.B3_active[1, 1] + float(additional_cost) * change_to_game3

        if game_played == 2 and game_affected == 1:
            change_to_game1 = float(self.TotalGameCostCorrelation_2_to_1.get())
            self.A1_active[0, 0] = self.A1_active[0, 0] + float(additional_cost) * change_to_game1
            self.A1_active[0, 1] = self.A1_active[0, 1] + float(additional_cost) * change_to_game1
            self.A1_active[1, 0] = self.A1_active[1, 0] + float(additional_cost) * change_to_game1
            self.A1_active[1, 1] = self.A1_active[1, 1] + float(additional_cost) * change_to_game1

            self.B1_active[0, 0] = self.B1_active[0, 0] + float(additional_cost) * change_to_game1
            self.B1_active[0, 1] = self.B1_active[0, 1] + float(additional_cost) * change_to_game1
            self.B1_active[1, 0] = self.B1_active[1, 0] + float(additional_cost) * change_to_game1
            self.B1_active[1, 1] = self.B1_active[1, 1] + float(additional_cost) * change_to_game1

        if game_played == 2 and game_affected == 3:
            change_to_game3 = float(self.TotalGameCostCorrelation_2_to_3.get())
            self.A3_active[0, 0] = self.A3_active[0, 0] + float(additional_cost) * change_to_game3
            self.A3_active[0, 1] = self.A3_active[0, 1] + float(additional_cost) * change_to_game3
            self.A3_active[1, 0] = self.A3_active[1, 0] + float(additional_cost) * change_to_game3
            self.A3_active[1, 1] = self.A3_active[1, 1] + float(additional_cost) * change_to_game3

            self.B3_active[0, 0] = self.B3_active[0, 0] + float(additional_cost) * change_to_game3
            self.B3_active[0, 1] = self.B3_active[0, 1] + float(additional_cost) * change_to_game3
            self.B3_active[1, 0] = self.B3_active[1, 0] + float(additional_cost) * change_to_game3
            self.B3_active[1, 1] = self.B3_active[1, 1] + float(additional_cost) * change_to_game3

        if game_played == 3 and game_affected ==1:
            change_to_game1 = float(self.TotalGameCostCorrelation_3_to_1.get())
            self.A1_active[0, 0] = self.A1_active[0, 0] + float(additional_cost) * change_to_game1
            self.A1_active[0, 1] = self.A1_active[0, 1] + float(additional_cost) * change_to_game1
            self.A1_active[1, 0] = self.A1_active[1, 0] + float(additional_cost) * change_to_game1
            self.A1_active[1, 1] = self.A1_active[1, 1] + float(additional_cost) * change_to_game1

            self.B1_active[0, 0] = self.B1_active[0, 0] + float(additional_cost) * change_to_game1
            self.B1_active[0, 1] = self.B1_active[0, 1] + float(additional_cost) * change_to_game1
            self.B1_active[1, 0] = self.B1_active[1, 0] + float(additional_cost) * change_to_game1
            self.B1_active[1, 1] = self.B1_active[1, 1] + float(additional_cost) * change_to_game1

        if game_played == 3 and game_affected == 2:
            change_to_game2 = float(self.TotalGameCostCorrelation_3_to_2.get())
            self.A2_active[0, 0] = self.A2_active[0, 0] + float(additional_cost) * change_to_game2
            self.A2_active[0, 1] = self.A2_active[0, 1] + float(additional_cost) * change_to_game2
            self.A2_active[1, 0] = self.A2_active[1, 0] + float(additional_cost) * change_to_game2
            self.A2_active[1, 1] = self.A2_active[1, 1] + float(additional_cost) * change_to_game2

            self.B2_active[0, 0] = self.B2_active[0, 0] + float(additional_cost) * change_to_game2
            self.B2_active[0, 1] = self.B2_active[0, 1] + float(additional_cost) * change_to_game2
            self.B2_active[1, 0] = self.B2_active[1, 0] + float(additional_cost) * change_to_game2
            self.B2_active[1, 1] = self.B2_active[1, 1] + float(additional_cost) * change_to_game2

        return

    def datasetup(self):

        # data set up

        self.Data_set_up = tkinter.LabelFrame(self.myFrame, text="Data Set Up")
        self.Data_set_up.grid(row=0, column=0)

        # probability set up

        # game 1

        self.Probability_set_up = tkinter.LabelFrame(self.Data_set_up, text="Probability Set Up")
        self.Probability_set_up.grid(row=0, column=0, padx=10, pady=10)

        self.Probability_of_PlayerA_defecting_label = tkinter.Label(self.Probability_set_up,
                                                                    text="Probability of A defecting")
        self.Probability_of_PlayerA_defecting_label.grid(row=1, column=0)

        self.Probability_of_PlayerA_defecting_label = tkinter.Label(self.Probability_set_up, text="Game 1")
        self.Probability_of_PlayerA_defecting_label.grid(row=0, column=1)

        self.Probability_of_PlayerB_defecting_label = tkinter.Label(self.Probability_set_up,
                                                                    text="Probability of B defecting")
        self.Probability_of_PlayerB_defecting_label.grid(row=2, column=0)

        self.Probability_of_PlayerA_defecting_game1 = tkinter.Entry(self.Probability_set_up)
        self.Probability_of_PlayerA_defecting_game1.insert(0, 0.5)
        self.Probability_of_PlayerA_defecting_game1.grid(row=1, column=1)

        self.Probability_of_PlayerB_defecting_game1 = tkinter.Entry(self.Probability_set_up)
        self.Probability_of_PlayerB_defecting_game1.insert(0, 0.5)
        self.Probability_of_PlayerB_defecting_game1.grid(row=2, column=1)

        # game 2

        self.Probability_of_PlayerA_defecting_label = tkinter.Label(self.Probability_set_up, text="Game 2")
        self.Probability_of_PlayerA_defecting_label.grid(row=0, column=4)

        self.Probability_of_PlayerA_defecting_game2 = tkinter.Entry(self.Probability_set_up)
        self.Probability_of_PlayerA_defecting_game2.insert(0, 0.5)
        self.Probability_of_PlayerA_defecting_game2.grid(row=1, column=4)

        self.Probability_of_PlayerB_defecting_game2 = tkinter.Entry(self.Probability_set_up)
        self.Probability_of_PlayerB_defecting_game2.insert(0, 0.5)
        self.Probability_of_PlayerB_defecting_game2.grid(row=2, column=4)

        # game 3

        self.Probability_of_PlayerA_defecting_label = tkinter.Label(self.Probability_set_up, text="Game 3")
        self.Probability_of_PlayerA_defecting_label.grid(row=0, column=5)

        self.Probability_of_PlayerA_defecting_game3 = tkinter.Entry(self.Probability_set_up)
        self.Probability_of_PlayerA_defecting_game3.insert(0, 0.5)
        self.Probability_of_PlayerA_defecting_game3.grid(row=1, column=5)

        self.Probability_of_PlayerB_defecting_game3 = tkinter.Entry(self.Probability_set_up)
        self.Probability_of_PlayerB_defecting_game3.insert(0, 0.5)
        self.Probability_of_PlayerB_defecting_game3.grid(row=2, column=5)

        # game set up data

        self.Game_parameters = tkinter.LabelFrame(self.Data_set_up, text="Game Parameters")
        self.Game_parameters.grid(row=0, column=1)

        self.Maximum_Survivable_game_cost_label = tkinter.Label(self.Game_parameters, text="Maximum Survivable Cost ")
        self.Maximum_Survivable_game_cost_label.grid(row=0, column=0, padx=50)

        self.Maximum_Survivable_game_cost_game1 = tkinter.Entry(self.Game_parameters)
        self.Maximum_Survivable_game_cost_game1.insert(0, 1000)
        self.Maximum_Survivable_game_cost_game1.grid(row=0, column=1)

        self.Maximum_Survivable_game_cost_game2 = tkinter.Entry(self.Game_parameters)
        self.Maximum_Survivable_game_cost_game2.insert(0, 1000)
        self.Maximum_Survivable_game_cost_game2.grid(row=0, column=2)

        self.Maximum_Survivable_game_cost_game3 = tkinter.Entry(self.Game_parameters)
        self.Maximum_Survivable_game_cost_game3.insert(0, 1000)
        self.Maximum_Survivable_game_cost_game3.grid(row=0, column=3)

        self.Fraction_of_cost_carried_forward_to_next_round_label = tkinter.Label(self.Game_parameters,
                                                                                  text="Fraction game total carried forward to next round")
        self.Fraction_of_cost_carried_forward_to_next_round_label.grid(row=1, column=0)

        self.Fraction_of_cost_carried_forward_to_next_round_game1 = tkinter.Entry(self.Game_parameters)
        self.Fraction_of_cost_carried_forward_to_next_round_game1.insert(0, 1)
        self.Fraction_of_cost_carried_forward_to_next_round_game1.grid(row=1, column=1)

        self.Fraction_of_cost_carried_forward_to_next_round_game2 = tkinter.Entry(self.Game_parameters)
        self.Fraction_of_cost_carried_forward_to_next_round_game2.insert(0, 1)
        self.Fraction_of_cost_carried_forward_to_next_round_game2.grid(row=1, column=2)

        self.Fraction_of_cost_carried_forward_to_next_round_game3 = tkinter.Entry(self.Game_parameters)
        self.Fraction_of_cost_carried_forward_to_next_round_game3.insert(0, 1)
        self.Fraction_of_cost_carried_forward_to_next_round_game3.grid(row=1, column=3)

        self.Include_competitive_disadvantage_in_analysis_label = tkinter.Label(self.Game_parameters,
                                                                                text="Proportion to add to max loss. 1= complete addition")
        self.Include_competitive_disadvantage_in_analysis_label.grid(row=2, column=0)

        self.Include_competitive_disadvantage_in_analysis_game1 = tkinter.Entry(self.Game_parameters)
        self.Include_competitive_disadvantage_in_analysis_game1.insert(0, 1)
        self.Include_competitive_disadvantage_in_analysis_game1.grid(row=2, column=1)

        self.Include_competitive_disadvantage_in_analysis_game2 = tkinter.Entry(self.Game_parameters)
        self.Include_competitive_disadvantage_in_analysis_game2.insert(0, 1)
        self.Include_competitive_disadvantage_in_analysis_game2.grid(row=2, column=2)

        self.Include_competitive_disadvantage_in_analysis_game3 = tkinter.Entry(self.Game_parameters)
        self.Include_competitive_disadvantage_in_analysis_game3.insert(0, 1)
        self.Include_competitive_disadvantage_in_analysis_game3.grid(row=2, column=3)


        self.Number_of_rounds_label = tkinter.Label(self.Game_parameters, text="Number of rounds")
        self.Number_of_rounds_label.grid(row=4, column=0)

        self.Number_of_rounds = tkinter.Entry(self.Game_parameters)
        self.Number_of_rounds.grid(row=4, column=1)

        # Cost set up frame

        self.Matrix = tkinter.LabelFrame(self.myFrame, text="Cost Set Up")
        self.Matrix.grid(row=1, column=0, padx=10, pady=10)

        # Matrix 1 data set up

        self.Index_label = tkinter.Label(self.Matrix, text=" Key = (Player A, Player B) ")
        self.Index_label.grid(row=0, column=0)

        self.PlayerB_label = tkinter.Label(self.Matrix, text="Player B Defects")
        self.PlayerB_label.grid(row=1, column=1)
        self.PlayerB_label = tkinter.Label(self.Matrix, text="Player B Cooperates")
        self.PlayerB_label.grid(row=1, column=2)

        self.PlayerA_label = tkinter.Label(self.Matrix, text="Player A Defects")
        self.PlayerA_label.grid(row=2, column=0)
        self.PlayerA_label = tkinter.Label(self.Matrix, text="Player A Cooperates")
        self.PlayerA_label.grid(row=3, column=0)

        self.Cell_11 = tkinter.LabelFrame(self.Matrix)
        self.Cell_11.grid(row=2, column=1)

        self.PlayerADefectCostIfPlayerBDefects1 = tkinter.Entry(self.Cell_11, width=10)
        self.PlayerADefectCostIfPlayerBDefects1.insert(0, 8)
        self.PlayerADefectCostIfPlayerBDefects1.grid(row=0, column=0)

        self.PlayerBDefectCostIfPlayerADefects1 = tkinter.Entry(self.Cell_11, width=10)
        self.PlayerBDefectCostIfPlayerADefects1.insert(0, 8)
        self.PlayerBDefectCostIfPlayerADefects1.grid(row=0, column=1)

        self.Cell_21 = tkinter.LabelFrame(self.Matrix)
        self.Cell_21.grid(row=2, column=2)

        self.PlayerADefectCostIfPlayerBCooperates1 = tkinter.Entry(self.Cell_21, width=10)
        self.PlayerADefectCostIfPlayerBCooperates1.insert(0, 1)
        self.PlayerADefectCostIfPlayerBCooperates1.grid(row=0, column=0)

        self.PlayerBCooperatesCostIfPlayerADefects1 = tkinter.Entry(self.Cell_21, width=10)
        self.PlayerBCooperatesCostIfPlayerADefects1.insert(0, 10)
        self.PlayerBCooperatesCostIfPlayerADefects1.grid(row=0, column=1)

        self.Cell_12 = tkinter.LabelFrame(self.Matrix)
        self.Cell_12.grid(row=3, column=1)

        self.PlayerACooperatesCostIfPlayerBDefects1 = tkinter.Entry(self.Cell_12, width=10)
        self.PlayerACooperatesCostIfPlayerBDefects1.insert(0, 10)
        self.PlayerACooperatesCostIfPlayerBDefects1.grid(row=0, column=0)

        self.PlayerBDefectsCostIfPlayerACooperates1 = tkinter.Entry(self.Cell_12, width=10)
        self.PlayerBDefectsCostIfPlayerACooperates1.insert(0, 1)
        self.PlayerBDefectsCostIfPlayerACooperates1.grid(row=0, column=1)

        self.Cell_22 = tkinter.LabelFrame(self.Matrix)
        self.Cell_22.grid(row=3, column=2)

        self.PlayerACooperatesCostIfPlayerBCooperates1 = tkinter.Entry(self.Cell_22, width=10)
        self.PlayerACooperatesCostIfPlayerBCooperates1.insert(0, 2)
        self.PlayerACooperatesCostIfPlayerBCooperates1.grid(row=0, column=0)

        self.PlayerBCooperatesCostIfPlayerACooperates1 = tkinter.Entry(self.Cell_22, width=10)
        self.PlayerBCooperatesCostIfPlayerACooperates1.insert(0, 2)
        self.PlayerBCooperatesCostIfPlayerACooperates1.grid(row=0, column=1)

        self.Data_entry_button = tkinter.Button(self.myFrame, text="Commence analysis", command=self.analyse)
        self.Data_entry_button.grid(row=2, column=0)

        # Matrix 2 data set up

        self.PlayerB_label = tkinter.Label(self.Matrix, text="Player B Defects")
        self.PlayerB_label.grid(row=1, column=5)
        self.PlayerB_label = tkinter.Label(self.Matrix, text="Player B Cooperates")
        self.PlayerB_label.grid(row=1, column=6)

        self.PlayerA_label = tkinter.Label(self.Matrix, text=" ")
        self.PlayerA_label.grid(row=2, column=4)
        self.PlayerA_label = tkinter.Label(self.Matrix, text=" ")
        self.PlayerA_label.grid(row=3, column=4)

        self.Cell_11 = tkinter.LabelFrame(self.Matrix)
        self.Cell_11.grid(row=2, column=5)

        self.PlayerADefectCostIfPlayerBDefects2 = tkinter.Entry(self.Cell_11, width=10)
        self.PlayerADefectCostIfPlayerBDefects2.insert(0, 8)
        self.PlayerADefectCostIfPlayerBDefects2.grid(row=0, column=0)

        self.PlayerBDefectCostIfPlayerADefects2 = tkinter.Entry(self.Cell_11, width=10)
        self.PlayerBDefectCostIfPlayerADefects2.insert(0, 8)
        self.PlayerBDefectCostIfPlayerADefects2.grid(row=0, column=1)

        self.Cell_21 = tkinter.LabelFrame(self.Matrix)
        self.Cell_21.grid(row=2, column=6)

        self.PlayerADefectCostIfPlayerBCooperates2 = tkinter.Entry(self.Cell_21, width=10)
        self.PlayerADefectCostIfPlayerBCooperates2.insert(0, 1)
        self.PlayerADefectCostIfPlayerBCooperates2.grid(row=0, column=0)

        self.PlayerBCooperatesCostIfPlayerADefects2 = tkinter.Entry(self.Cell_21, width=10)
        self.PlayerBCooperatesCostIfPlayerADefects2.insert(0, 10)
        self.PlayerBCooperatesCostIfPlayerADefects2.grid(row=0, column=1)

        self.Cell_12 = tkinter.LabelFrame(self.Matrix)
        self.Cell_12.grid(row=3, column=5)

        self.PlayerACooperatesCostIfPlayerBDefects2 = tkinter.Entry(self.Cell_12, width=10)
        self.PlayerACooperatesCostIfPlayerBDefects2.insert(0, 10)
        self.PlayerACooperatesCostIfPlayerBDefects2.grid(row=0, column=0)

        self.PlayerBDefectsCostIfPlayerACooperates2 = tkinter.Entry(self.Cell_12, width=10)
        self.PlayerBDefectsCostIfPlayerACooperates2.insert(0, 1)
        self.PlayerBDefectsCostIfPlayerACooperates2.grid(row=0, column=1)

        self.Cell_22 = tkinter.LabelFrame(self.Matrix)
        self.Cell_22.grid(row=3, column=6)

        self.PlayerACooperatesCostIfPlayerBCooperates2 = tkinter.Entry(self.Cell_22, width=10)
        self.PlayerACooperatesCostIfPlayerBCooperates2.insert(0, 2)
        self.PlayerACooperatesCostIfPlayerBCooperates2.grid(row=0, column=0)

        self.PlayerBCooperatesCostIfPlayerACooperates2 = tkinter.Entry(self.Cell_22, width=10)
        self.PlayerBCooperatesCostIfPlayerACooperates2.insert(0, 2)
        self.PlayerBCooperatesCostIfPlayerACooperates2.grid(row=0, column=1)

        # Matrix 3 set up

        self.PlayerB_label = tkinter.Label(self.Matrix, text="Player B Defects")
        self.PlayerB_label.grid(row=1, column=8)
        self.PlayerB_label = tkinter.Label(self.Matrix, text="Player B Cooperates")
        self.PlayerB_label.grid(row=1, column=9)

        self.PlayerA_label = tkinter.Label(self.Matrix, text=" ")
        self.PlayerA_label.grid(row=2, column=7)
        self.PlayerA_label = tkinter.Label(self.Matrix, text=" ")
        self.PlayerA_label.grid(row=3, column=7)

        self.Cell_11 = tkinter.LabelFrame(self.Matrix)
        self.Cell_11.grid(row=2, column=8)

        self.PlayerADefectCostIfPlayerBDefects3 = tkinter.Entry(self.Cell_11, width=10)
        self.PlayerADefectCostIfPlayerBDefects3.insert(0, 8)
        self.PlayerADefectCostIfPlayerBDefects3.grid(row=0, column=0)

        self.PlayerBDefectCostIfPlayerADefects3 = tkinter.Entry(self.Cell_11, width=10)
        self.PlayerBDefectCostIfPlayerADefects3.insert(0, 8)
        self.PlayerBDefectCostIfPlayerADefects3.grid(row=0, column=1)

        self.Cell_21 = tkinter.LabelFrame(self.Matrix)
        self.Cell_21.grid(row=2, column=9)

        self.PlayerADefectCostIfPlayerBCooperates3 = tkinter.Entry(self.Cell_21, width=10)
        self.PlayerADefectCostIfPlayerBCooperates3.insert(0, 1)
        self.PlayerADefectCostIfPlayerBCooperates3.grid(row=0, column=0)

        self.PlayerBCooperatesCostIfPlayerADefects3 = tkinter.Entry(self.Cell_21, width=10)
        self.PlayerBCooperatesCostIfPlayerADefects3.insert(0, 10)
        self.PlayerBCooperatesCostIfPlayerADefects3.grid(row=0, column=1)

        self.Cell_12 = tkinter.LabelFrame(self.Matrix)
        self.Cell_12.grid(row=3, column=8)

        self.PlayerACooperatesCostIfPlayerBDefects3 = tkinter.Entry(self.Cell_12, width=10)
        self.PlayerACooperatesCostIfPlayerBDefects3.insert(0, 10)
        self.PlayerACooperatesCostIfPlayerBDefects3.grid(row=0, column=0)

        self.PlayerBDefectsCostIfPlayerACooperates3 = tkinter.Entry(self.Cell_12, width=10)
        self.PlayerBDefectsCostIfPlayerACooperates3.insert(0, 1)
        self.PlayerBDefectsCostIfPlayerACooperates3.grid(row=0, column=1)

        self.Cell_22 = tkinter.LabelFrame(self.Matrix)
        self.Cell_22.grid(row=3, column=9)

        self.PlayerACooperatesCostIfPlayerBCooperates3 = tkinter.Entry(self.Cell_22, width=10)
        self.PlayerACooperatesCostIfPlayerBCooperates3.insert(0, 2)
        self.PlayerACooperatesCostIfPlayerBCooperates3.grid(row=0, column=0)

        self.PlayerBCooperatesCostIfPlayerACooperates3 = tkinter.Entry(self.Cell_22, width=10)
        self.PlayerBCooperatesCostIfPlayerACooperates3.insert(0, 2)
        self.PlayerBCooperatesCostIfPlayerACooperates3.grid(row=0, column=1)

        # Correlation set up frame - changing the total cost of a game based on other games

        self.CorrelationMatices = tkinter.LabelFrame(self.myFrame, text="Correlations")
        self.CorrelationMatices.grid(row=2, column=0, padx=5)

        self.TotalCostCorrelation = tkinter.LabelFrame(self.CorrelationMatices, text="Total Cost Correlations")
        self.TotalCostCorrelation.grid(row=0, column=0)

        # self.gamePayedlabel = tkinter.Label(self.TotalCostCorrelation, text="Total Cost Correlation")
        # self.gamePayedlabel.grid(row=0, column=0)

        self.gamePayedlabel = tkinter.Label(self.TotalCostCorrelation, text="Played")
        self.gamePayedlabel.grid(row=1, column=3)

        self.gameEffectedLabel = tkinter.Label(self.TotalCostCorrelation, text="Game effected")
        self.gameEffectedLabel.grid(row=4, column=0)

        self.GamePlayed1Label = tkinter.Label(self.TotalCostCorrelation, text="1")
        self.GamePlayed1Label.grid(row=2, column=2)

        self.GamePlayed2Label = tkinter.Label(self.TotalCostCorrelation, text="2")
        self.GamePlayed2Label.grid(row=2, column=3)

        self.GamePlayed3Label = tkinter.Label(self.TotalCostCorrelation, text="3")
        self.GamePlayed3Label.grid(row=2, column=4)

        self.GameEffected1Label = tkinter.Label(self.TotalCostCorrelation, text="1")
        self.GameEffected1Label.grid(row=3, column=1)

        self.GameEffected2Label = tkinter.Label(self.TotalCostCorrelation, text="2")
        self.GameEffected2Label.grid(row=4, column=1)

        self.GameEffected3Label = tkinter.Label(self.TotalCostCorrelation, text="3")
        self.GameEffected3Label.grid(row=5, column=1)

        self.TotalGameCostCorrelation_1_to_1 = tkinter.Entry(self.TotalCostCorrelation, width=5)
        self.TotalGameCostCorrelation_1_to_1.insert(0, "-")
        self.TotalGameCostCorrelation_1_to_1.grid(row=3, column=2)

        self.TotalGameCostCorrelation_1_to_2 = tkinter.Entry(self.TotalCostCorrelation, width=5)
        self.TotalGameCostCorrelation_1_to_2.insert(0, 1)
        self.TotalGameCostCorrelation_1_to_2.grid(row=4, column=2)

        self.TotalGameCostCorrelation_1_to_3 = tkinter.Entry(self.TotalCostCorrelation, width=5)
        self.TotalGameCostCorrelation_1_to_3.insert(0, 1)
        self.TotalGameCostCorrelation_1_to_3.grid(row=5, column=2)

        self.TotalGameCostCorrelation_2_to_1 = tkinter.Entry(self.TotalCostCorrelation, width=5)
        self.TotalGameCostCorrelation_2_to_1.insert(0, 1)
        self.TotalGameCostCorrelation_2_to_1.grid(row=3, column=3)

        self.TotalGameCostCorrelation_2_to_2 = tkinter.Entry(self.TotalCostCorrelation, width=5)
        self.TotalGameCostCorrelation_2_to_2.insert(0, "-")
        self.TotalGameCostCorrelation_2_to_2.grid(row=4, column=3)

        self.TotalGameCostCorrelation_2_to_3 = tkinter.Entry(self.TotalCostCorrelation, width=5)
        self.TotalGameCostCorrelation_2_to_3.insert(0, 1)
        self.TotalGameCostCorrelation_2_to_3.grid(row=5, column=3)

        self.TotalGameCostCorrelation_3_to_1 = tkinter.Entry(self.TotalCostCorrelation, width=5)
        self.TotalGameCostCorrelation_3_to_1.insert(0, 1)
        self.TotalGameCostCorrelation_3_to_1.grid(row=3, column=4)

        self.TotalGameCostCorrelation_3_to_2 = tkinter.Entry(self.TotalCostCorrelation, width=5)
        self.TotalGameCostCorrelation_3_to_2.insert(0, 1)
        self.TotalGameCostCorrelation_3_to_2.grid(row=4, column=4)

        self.TotalGameCostCorrelation_3_to_3 = tkinter.Entry(self.TotalCostCorrelation, width=5)
        self.TotalGameCostCorrelation_3_to_3.insert(0, "-")
        self.TotalGameCostCorrelation_3_to_3.grid(row=5, column=4)

        # set up matrices for competitive loss

        self.CompetitiveCostCorrelation = tkinter.LabelFrame(self.CorrelationMatices,
                                                             text="Competitive Cost Correlations")
        self.CompetitiveCostCorrelation.grid(row=0, column=1, padx=5)

        # self.gamePayedlabel = tkinter.Label(self.CompetitiveCostCorrelation, text="Competitive loss correlation")
        # self.gamePayedlabel.grid(row=0, column=6)

        self.gamePayedlabel = tkinter.Label(self.CompetitiveCostCorrelation, text="Played")
        self.gamePayedlabel.grid(row=1, column=9)

        self.GamePlayed1Label = tkinter.Label(self.CompetitiveCostCorrelation, text="1")
        self.GamePlayed1Label.grid(row=2, column=8)

        self.GamePlayed2Label = tkinter.Label(self.CompetitiveCostCorrelation, text="2")
        self.GamePlayed2Label.grid(row=2, column=9)

        self.GamePlayed3Label = tkinter.Label(self.CompetitiveCostCorrelation, text="3")
        self.GamePlayed3Label.grid(row=2, column=10)

        self.GameEffected1Label = tkinter.Label(self.CompetitiveCostCorrelation, text="1")
        self.GameEffected1Label.grid(row=3, column=7)

        self.GameEffected2Label = tkinter.Label(self.CompetitiveCostCorrelation, text="2")
        self.GameEffected2Label.grid(row=4, column=7)

        self.GameEffected3Label = tkinter.Label(self.CompetitiveCostCorrelation, text="3")
        self.GameEffected3Label.grid(row=5, column=7)

        self.CompetitiveCorrelation_1_to_1 = tkinter.Entry(self.CompetitiveCostCorrelation, width=5)
        self.CompetitiveCorrelation_1_to_1.insert(0, "-")
        self.CompetitiveCorrelation_1_to_1.grid(row=3, column=8)

        self.CompetitiveCorrelation_1_to_2 = tkinter.Entry(self.CompetitiveCostCorrelation, width=5)
        self.CompetitiveCorrelation_1_to_2.insert(0, 1)
        self.CompetitiveCorrelation_1_to_2.grid(row=4, column=8)

        self.CompetitiveCorrelation_1_to_3 = tkinter.Entry(self.CompetitiveCostCorrelation, width=5)
        self.CompetitiveCorrelation_1_to_3.insert(0, 1)
        self.CompetitiveCorrelation_1_to_3.grid(row=5, column=8)

        self.CompetitiveCorrelation_2_to_1 = tkinter.Entry(self.CompetitiveCostCorrelation, width=5)
        self.CompetitiveCorrelation_2_to_1.insert(0, 1)
        self.CompetitiveCorrelation_2_to_1.grid(row=3, column=9)

        self.CompetitiveCorrelation_2_to_2 = tkinter.Entry(self.CompetitiveCostCorrelation, width=5)
        self.CompetitiveCorrelation_2_to_2.insert(0, "-")
        self.CompetitiveCorrelation_2_to_2.grid(row=4, column=9)

        self.CompetitiveCorrelation_2_to_3 = tkinter.Entry(self.CompetitiveCostCorrelation, width=5)
        self.CompetitiveCorrelation_2_to_3.insert(0, 1)
        self.CompetitiveCorrelation_2_to_3.grid(row=5, column=9)

        self.CompetitiveCorrelation_3_to_1 = tkinter.Entry(self.CompetitiveCostCorrelation, width=5)
        self.CompetitiveCorrelation_3_to_1.insert(0, 1)
        self.CompetitiveCorrelation_3_to_1.grid(row=3, column=10)

        self.CompetitiveCorrelation_3_to_2 = tkinter.Entry(self.CompetitiveCostCorrelation, width=5)
        self.CompetitiveCorrelation_3_to_2.insert(0, 1)
        self.CompetitiveCorrelation_3_to_2.grid(row=4, column=10)

        self.CompetitiveCorrelation_3_to_3 = tkinter.Entry(self.CompetitiveCostCorrelation, width=5)
        self.CompetitiveCorrelation_3_to_3.insert(0, "-")
        self.CompetitiveCorrelation_3_to_3.grid(row=5, column=10)

        # add button

        self.Data_entry_button = tkinter.Button(self.myFrame, text="Commence analysis", command=self.analyse)
        self.Data_entry_button.grid(row=3, column=0)

    def determineIfAorBDefect(self, ProbA, ProbB):  # this function determines if A and B co-operate of defect

        A_defects = False
        B_defects = False

        A_defects_status = random.random()
        if A_defects_status <= ProbA:
            A_defects = True
        print("A defects", A_defects)

        B_defects_status = random.random()
        if B_defects_status <= ProbB:
            B_defects = True
        print("B defects", B_defects)

        return [A_defects, B_defects]

    def DetermineCosts(self, A_defects, B_defects, A, B):  # This module determines the cost to each player

        print("A status ", A_defects)
        print("B status ", B_defects)
        # cost to players
        # both defect
        if A_defects == True:
            if B_defects == True:
                Cost_A = A[0, 0]
                Cost_B = B[0, 0]
            # A defects and B co-operates
            elif B_defects == False:
                Cost_A = A[0, 1]
                Cost_B = B[0, 1]
                # Competitive_disadvantage_B = (Cost_B - Cost_A) * float(
                #    self.Fraction_of_competitive_disadvantage.get())

        # A co-operates and B defects
        elif A_defects == False:
            if B_defects == True:
                Cost_A = A[1, 0]
                Cost_B = B[1, 0]
                # Competitive_disadvantage_A = (Cost_A - Cost_B) * float(
                #    self.Fraction_of_competitive_disadvantage.get())
            # A co-operates and B co-operates
            elif B_defects == False:
                Cost_A = A[1, 1]
                Cost_B = B[1, 1]
        return (Cost_A, Cost_B)

    def CaclculateNewProbabilityBasedOnTotaCost(self, initalProbabilty, MaximumSustainableCost, CurrentCost):

        # use equation of a straight line to establish new probabilities as the Current cost increases.

        gradientOfLine = (1 - float(initalProbabilty)) / float(MaximumSustainableCost)
        newProbability = CurrentCost * gradientOfLine + initalProbabilty

        # set limits on the probability.

        if newProbability > 1:
            newProbability = 1

        if newProbability < 0:
            newProbability = 0

        return newProbability

    def PlotGraphs(self):

        #summary data

        self.summaryData = tkinter.LabelFrame(self.myFrame2, text="Outputs")
        self.summaryData.grid(row=1, column=0)

        self.numberOfRoundsPlayed_label = tkinter.Label(self.summaryData, text="Number of Rounds played = ")
        self.numberOfRoundsPlayed_label.grid(row=0, column=0)

        NumberOfRoundsText = str(self.NumberOfRounds[-1])

        self.numberOfRoundsPlayed_label = tkinter.Label(self.summaryData, text=NumberOfRoundsText)
        self.numberOfRoundsPlayed_label.grid(row=0, column=1)

        #set up space for graphs

        self.Output = tkinter.LabelFrame(self.myFrame2, text="Outputs")
        self.Output.grid(row=0, column=0)



        # Results



        # Plot graphs for game 1

        # total costs
        fig = Figure(figsize=(3, 2), dpi=100)
        fig.add_subplot(111).plot(self.NumberOfRounds, self.CummulativeTotalCostGame1)
        textstg = "Max cost = " + str(self.TotalCostGame1)
        fig.text(0.5, 0.8, textstg, horizontalalignment='center', verticalalignment='center')
        fig.suptitle("Total Costs Game 1")


        # plt.ylabel('Total cost of the game')
        # plt.xlabel("Negotiating Round")
        # plt.title("Total Cost")

        canvas = FigureCanvasTkAgg(fig, master=self.Output)  # A tk.DrawingArea.

        #canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
        #frame = tk.Frame(canvas, background="#ffffff")
        #vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
        #canvas.configure(yscrollcommand=vsb.set)

        #vsb.pack(side="right", fill="y")
        #canvas.pack(side="left", fill="both", expand=True)


        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column= 0)

        # probabilities
        fig = Figure(figsize=(3, 2), dpi=100)
        fig.add_subplot(111).plot(self.NumberOfRounds, self.ListOfProbOfA_game1, self.NumberOfRounds,
                                  self.ListOfProbOfB_game1)
        fig.suptitle("Game 1 probabilities")
        #fig.legend()

        canvas = FigureCanvasTkAgg(fig, master=self.Output)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=1)

        # costs for Players A and B
        fig = Figure(figsize=(3, 2), dpi=100)
        fig.add_subplot(111).plot(self.NumberOfRounds, self.CummualativeCostOfPlayerAGame1, self.NumberOfRounds,
                                  self.CummualativeCostOfPlayerBGame1)
        fig.suptitle("Game 1 Player Costs")

        canvas = FigureCanvasTkAgg(fig, master=self.Output)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=2)

        # Plot graphs for game 2

        fig = Figure(figsize=(3, 2), dpi=100)
        fig.add_subplot(111).plot(self.NumberOfRounds, self.CummulativeTotalCostGame2)
        textstg = "Max cost = " + str(self.TotalCostGame2)
        fig.text(0.5, 0.8, textstg, horizontalalignment='center', verticalalignment='center')
        fig.suptitle("Total Costs Game 2")

        # plt.ylabel('Total cost of the game')
        # plt.xlabel("Negotiating Round")
        # plt.title("Total Cost")

        canvas = FigureCanvasTkAgg(fig, master=self.Output)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0)

        # Total Costs

        fig = Figure(figsize=(3, 2), dpi=100)
        fig.add_subplot(111).plot(self.NumberOfRounds, self.CummulativeTotalCostGame2)
        textstg = "Max cost = " + str(self.TotalCostGame2)
        fig.text(0.5, 0.8, textstg, horizontalalignment='center', verticalalignment='center')
        fig.suptitle("Total Costs Game 2")

        # plt.ylabel('Total cost of the game')
        # plt.xlabel("Negotiating Round")
        # plt.title("Total Cost")

        canvas = FigureCanvasTkAgg(fig, master=self.Output)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0)

        # probabilities
        fig = Figure(figsize=(3, 2), dpi=100)
        fig.add_subplot(111).plot(self.NumberOfRounds, self.ListOfProbOfA_game2, self.NumberOfRounds,
                                  self.ListOfProbOfB_game2)
        fig.suptitle("Game 2 probabilities")

        canvas = FigureCanvasTkAgg(fig, master=self.Output)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=1)


        # costs for Players A and B
        fig = Figure(figsize=(3, 2), dpi=100)
        fig.add_subplot(111).plot(self.NumberOfRounds, self.CummualativeCostOfPlayerAGame2, self.NumberOfRounds,
                                  self.CummualativeCostOfPlayerBGame2)
        fig.suptitle("Game 2 Player Costs")

        canvas = FigureCanvasTkAgg(fig, master=self.Output)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=2)

        # Plot graphs for game 3

        fig = Figure(figsize=(3, 2), dpi=100)
        fig.add_subplot(111).plot(self.NumberOfRounds, self.CummulativeTotalCostGame3)
        textstg = "Max cost = " + str(self.TotalCostGame3)
        fig.text(0.5, 0.8, textstg, horizontalalignment='center', verticalalignment='center')
        fig.suptitle("Total Costs Game 3")

        # plt.ylabel('Total cost of the game')
        # plt.xlabel("Negotiating Round")
        # plt.title("Total Cost")

        canvas = FigureCanvasTkAgg(fig, master=self.Output)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=2, column=0)

        # probabilities
        fig = Figure(figsize=(3, 2), dpi=100)
        fig.add_subplot(111).plot(self.NumberOfRounds, self.ListOfProbOfA_game3, self.NumberOfRounds,
                                  self.ListOfProbOfB_game3)
        fig.suptitle("Game 3 probabilities")

        canvas = FigureCanvasTkAgg(fig, master=self.Output)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=2, column=1)

        # costs for Players A and B
        fig = Figure(figsize=(3, 2), dpi=100)
        fig.add_subplot(111).plot(self.NumberOfRounds, self.CummualativeCostOfPlayerAGame3, self.NumberOfRounds,
                                  self.CummualativeCostOfPlayerBGame3)
        fig.suptitle("Game 3 Player Costs")

        canvas = FigureCanvasTkAgg(fig, master=self.Output)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=2, column=2)

        #summary data


    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def analyse(self):

        counter = 1
        LoopStatusComplete = False

        # Set start probabilities for each game

        Prob_of_A_defecting1 = float(self.Probability_of_PlayerA_defecting_game1.get())
        Prob_of_B_defecting1 = float(self.Probability_of_PlayerB_defecting_game1.get())

        Prob_of_A_defecting2 = float(self.Probability_of_PlayerA_defecting_game2.get())
        Prob_of_B_defecting2 = float(self.Probability_of_PlayerB_defecting_game2.get())

        Prob_of_A_defecting3 = float(self.Probability_of_PlayerA_defecting_game3.get())
        Prob_of_B_defecting3 = float(self.Probability_of_PlayerB_defecting_game3.get())

        self.ProbOfAdefectingInGame1 = Prob_of_A_defecting1
        self.ProbOfBdefectingInGame1 = Prob_of_B_defecting1

        self.ProbOfAdefectingInGame2 = Prob_of_A_defecting2
        self.ProbOfBdefectingInGame2 = Prob_of_B_defecting2

        self.ProbOfAdefectingInGame3 = Prob_of_A_defecting3
        self.ProbOfBdefectingInGame3 = Prob_of_B_defecting3

        # Build payoff matrices

        # matrix game 1

        CostToA_ADefectwithBdefect = float(self.PlayerADefectCostIfPlayerBDefects1.get())
        CostToB_BDefectwithAdefect = float(self.PlayerBDefectCostIfPlayerADefects1.get())
        CostToA_ADefectwithBCooperation = float(self.PlayerADefectCostIfPlayerBCooperates1.get())
        CostToB_BCooperateswithADefects = float(self.PlayerBCooperatesCostIfPlayerADefects1.get())
        CostToA_ACooperateswithBdefect = float(self.PlayerACooperatesCostIfPlayerBDefects1.get())
        CostToB_BDefectwithACooperates = float(self.PlayerBDefectsCostIfPlayerACooperates1.get())
        CostToA_ACooperateswithBCooperates = float(self.PlayerACooperatesCostIfPlayerBCooperates1.get())
        CostToB_BCooperateswithACooperates = float(self.PlayerBCooperatesCostIfPlayerACooperates1.get())

        A1 = np.array([[CostToA_ADefectwithBdefect, CostToA_ADefectwithBCooperation],
                       [CostToA_ACooperateswithBdefect, CostToA_ACooperateswithBCooperates]])
        B1 = np.array([[CostToB_BDefectwithAdefect, CostToB_BCooperateswithADefects],
                       [CostToB_BDefectwithACooperates, CostToB_BCooperateswithACooperates]])

        # matrix for game 2

        CostToA_ADefectwithBdefect = float(self.PlayerADefectCostIfPlayerBDefects2.get())
        CostToB_BDefectwithAdefect = float(self.PlayerBDefectCostIfPlayerADefects2.get())
        CostToA_ADefectwithBCooperation = float(self.PlayerADefectCostIfPlayerBCooperates2.get())
        CostToB_BCooperateswithADefects = float(self.PlayerBCooperatesCostIfPlayerADefects2.get())
        CostToA_ACooperateswithBdefect = float(self.PlayerACooperatesCostIfPlayerBDefects2.get())
        CostToB_BDefectwithACooperates = float(self.PlayerBDefectsCostIfPlayerACooperates2.get())
        CostToA_ACooperateswithBCooperates = float(self.PlayerACooperatesCostIfPlayerBCooperates2.get())
        CostToB_BCooperateswithACooperates = float(self.PlayerBCooperatesCostIfPlayerACooperates2.get())

        A2 = np.array([[CostToA_ADefectwithBdefect, CostToA_ADefectwithBCooperation],
                       [CostToA_ACooperateswithBdefect, CostToA_ACooperateswithBCooperates]])
        B2 = np.array([[CostToB_BDefectwithAdefect, CostToB_BCooperateswithADefects],
                       [CostToB_BDefectwithACooperates, CostToB_BCooperateswithACooperates]])

        # matrix for game 3

        CostToA_ADefectwithBdefect = float(self.PlayerADefectCostIfPlayerBDefects3.get())
        CostToB_BDefectwithAdefect = float(self.PlayerBDefectCostIfPlayerADefects3.get())
        CostToA_ADefectwithBCooperation = float(self.PlayerADefectCostIfPlayerBCooperates3.get())
        CostToB_BCooperateswithADefects = float(self.PlayerBCooperatesCostIfPlayerADefects3.get())
        CostToA_ACooperateswithBdefect = float(self.PlayerACooperatesCostIfPlayerBDefects3.get())
        CostToB_BDefectwithACooperates = float(self.PlayerBDefectsCostIfPlayerACooperates3.get())
        CostToA_ACooperateswithBCooperates = float(self.PlayerACooperatesCostIfPlayerBCooperates3.get())
        CostToB_BCooperateswithACooperates = float(self.PlayerBCooperatesCostIfPlayerACooperates3.get())

        A3 = np.array([[CostToA_ADefectwithBdefect, CostToA_ADefectwithBCooperation],
                       [CostToA_ACooperateswithBdefect, CostToA_ACooperateswithBCooperates]])
        B3 = np.array([[CostToB_BDefectwithAdefect, CostToB_BCooperateswithADefects],
                       [CostToB_BDefectwithACooperates, CostToB_BCooperateswithACooperates]])

          # set variables for cummulation to zero

        CummulativeCostGame1 = float(0)
        CummulativeCostGame2 = float(0)
        CummulativeCostGame3 = float(0)
        counter = 0
        self.NumberOfRounds = []
        self.CummulativeTotalCostGame1 = []
        self.CummulativeTotalCostGame2 = []
        self.CummulativeTotalCostGame3 = []
        self.ListOfProbOfA_game1 = []
        self.ListOfProbOfB_game1 = []
        self.ListOfProbOfA_game2 = []
        self.ListOfProbOfB_game2 = []
        self.ListOfProbOfA_game3 = []
        self.ListOfProbOfB_game3 = []
        self.TotalCostofPlayerAGame1 = 0
        self.TotalCostofPlayerBGame1 = 0
        self.TotalCostofPlayerAGame2 = 0
        self.TotalCostofPlayerBGame2 = 0
        self.TotalCostofPlayerAGame3 = 0
        self.TotalCostofPlayerBGame3 = 0

        self.cummulatedCompetitiveDisadvantageToPlayerAGame1 = 0
        self.cummulatedCompetitiveDisadvantageToPlayerBGame1 = 0
        self.cummulatedCompetitiveDisadvantageToPlayerAGame2 = 0
        self.cummulatedCompetitiveDisadvantageToPlayerBGame2 = 0
        self.cummulatedCompetitiveDisadvantageToPlayerAGame3 = 0
        self.cummulatedCompetitiveDisadvantageToPlayerBGame3 = 0



        TotalCostAdditiontoA1 = np.array([[0,0],[0,0]])
        TotalCostAdditiontoB1 = np.array([[0,0],[0,0]])
        TotalCostAdditiontoA3 = np.array([[0,0],[0,0]])
        TotalCostAdditiontoB3 = np.array([[0,0],[0,0]])
        TotalCostAdditiontoA3 = np.array([[0,0],[0,0]])
        TotalCostAdditiontoB3 = np.array([[0,0],[0,0]])

        print ("matrix test", float(TotalCostAdditiontoA1[1,0]))

        self.CummualativeCostOfPlayerAGame1 = []
        self.CummualativeCostOfPlayerBGame1 = []
        self.CummualativeCostOfPlayerAGame2 = []
        self.CummualativeCostOfPlayerBGame2 = []
        self.CummualativeCostOfPlayerAGame3 = []
        self.CummualativeCostOfPlayerBGame3 = []

        # cummulative costs to games from other games
        self.CostIncreaseToGame1fromGame2 = 0
        self.CostIncreaseToGame1fromGame3 = 0
        self.CostIncreaseToGame2fromGame1 = 0
        self.CostIncreaseToGame2fromGame3 = 0
        self.CostIncreaseToGame3fromGame1 = 0
        self.CostIncreaseToGame3fromGame2 = 0

        # set cumulated Disadvantage from Other Games

        self.CummuatedDisdvantageinGame1fromGame2_playerA = 0
        self.CummuatedDisdvantageinGame1fromGame3_playerA = 0
        self.CummuatedDisdvantageinGame2fromGame1_playerA = 0
        self.CummuatedDisdvantageinGame2fromGame3_playerA = 0
        self.CummuatedDisdvantageinGame3fromGame1_playerA = 0
        self.CummuatedDisdvantageinGame3fromGame2_playerA = 0

        self.CummuatedDisdvantageinGame1fromGame2_playerB = 0
        self.CummuatedDisdvantageinGame1fromGame3_playerB = 0
        self.CummuatedDisdvantageinGame2fromGame1_playerB = 0
        self.CummuatedDisdvantageinGame2fromGame3_playerB = 0
        self.CummuatedDisdvantageinGame3fromGame1_playerB = 0
        self.CummuatedDisdvantageinGame3fromGame2_playerB = 0

        # set matrices to be used in the loop

        self.A1_active = A1
        self.B1_active = B1
        self.A2_active = A2
        self.B2_active = B2
        self.A3_active = A3
        self.B3_active = B3

        self.TotalCostGame1 = float(0)
        self.TotalCostGame2 = float(0)
        self.TotalCostGame3 = float(0)

        # start loop

        while counter < int(self.Number_of_rounds.get()):

            # check against the maximum survivable costs that a loop can be run

            if self.TotalCostGame1 > float(self.Maximum_Survivable_game_cost_game1.get()):
                break

            if self.TotalCostGame2 > float(self.Maximum_Survivable_game_cost_game2.get()):
                break

            if self.TotalCostGame3 > float(self.Maximum_Survivable_game_cost_game3.get()):
                break

            GameOrder = self.determineGameOrder()
            print("-------------------------------------------------")
            print("Game Order= ", GameOrder)

            for x in range(3):
                print("Round = ", counter, " Game to be played=", GameOrder[x])

                if GameOrder[x] == 1:

                    # get probabilities of defecting for each player

                    #total cost impact from other games

                    costToPlayerAMaxfromgames2and3 = (self.CummuatedDisdvantageinGame1fromGame2_playerA * float(self.CompetitiveCorrelation_2_to_1.get())) \
                                                     + (self.CummuatedDisdvantageinGame1fromGame3_playerA * float(self.CompetitiveCorrelation_3_to_1.get()))

                    costToPlayerBMaxfromgames2and3 = (self.CummuatedDisdvantageinGame1fromGame2_playerB * float(self.CompetitiveCorrelation_2_to_1.get())) \
                                                     + (self.CummuatedDisdvantageinGame1fromGame3_playerB * float(self.CompetitiveCorrelation_3_to_1.get()))


                    TotalCostIncreaseToGame1 = self.CostIncreaseToGame1fromGame2+self.CostIncreaseToGame1fromGame3

                    probofPlayerA = self.CaclculateNewProbabilityBasedOnTotaCost(Prob_of_A_defecting1,
                                                                                 float(self.Maximum_Survivable_game_cost_game1.get()),
                                                                                 self.TotalCostGame1+self.cummulatedCompetitiveDisadvantageToPlayerAGame1
                                                                                 + TotalCostIncreaseToGame1 + costToPlayerAMaxfromgames2and3)
                    probofPlayerB = self.CaclculateNewProbabilityBasedOnTotaCost(Prob_of_B_defecting1,
                                                                                 float(self.Maximum_Survivable_game_cost_game1.get()),
                                                                                 self.TotalCostGame1+self.cummulatedCompetitiveDisadvantageToPlayerBGame1
                                                                                 + TotalCostIncreaseToGame1+costToPlayerBMaxfromgames2and3)

                    print ("total cost addition to A1", float(TotalCostAdditiontoA1[1, 0]))
                    print("total cost addition to B1", float(TotalCostAdditiontoB1[0, 1]))

                    playerStatus = self.determineIfAorBDefect(probofPlayerA, probofPlayerB)
                    print('Game number =', GameOrder[x], "=", playerStatus)
                    PlayerAStatusGame1 = playerStatus[0]
                    PlayerBStatusGame1 = playerStatus[1]

                    # we input the game status and the cost matrix to determine the game outcome for each player

                    GameOutCome = self.DetermineCosts(PlayerAStatusGame1, PlayerBStatusGame1, self.A1_active, self.B1_active)
                    print(GameOutCome)
                    print ("A1 Active = ", self.A1_active)
                    print ("B1 Active = ", self.B1_active)
                    fractionCarriedForward = float(self.Fraction_of_cost_carried_forward_to_next_round_game1.get())
                    CostofGame = float(GameOutCome[0]) + float(GameOutCome[1])
                    CostOfGame1CarriedForwardToNexRound = fractionCarriedForward * CostofGame / 2

                    # determine competitive disadvantage

                    # for player A

                    # find out if A has co-operated and B defected

                    if playerStatus[0] == False and playerStatus[1] == True:
                        print("A has co-operated and B defected", playerStatus[0], playerStatus[1])
                        self.competitiveDisadvantageToPlayerA_game1 = float(self.Include_competitive_disadvantage_in_analysis_game1.get()) * (
                                    float(GameOutCome[0]) - float(GameOutCome[1]))

                        # effect on player A's position in games 2 and 3

                        self.CummuatedDisdvantageinGame2fromGame1_playerA = self.CummuatedDisdvantageinGame2fromGame1_playerA + (
                                float(GameOutCome[0]) - float(GameOutCome[1]))
                        self.CummuatedDisdvantageinGame3fromGame1_playerA = self.CummuatedDisdvantageinGame3fromGame1_playerA + (
                            float(GameOutCome[0]) - float(GameOutCome[1]))

                    else:
                        self.competitiveDisadvantageToPlayerA_game1 = 0

                    # for player B

                    # find out if B has co-operated and A defected

                    if playerStatus[1] == False and playerStatus[0] == True:
                        self.competitiveDisadvantageToPlayerB_game1 = float(self.Include_competitive_disadvantage_in_analysis_game1.get()) * (
                                    float(GameOutCome[1]) - float(GameOutCome[0]))

                        # effect on player B's position in games 2 and 3

                        self.CummuatedDisdvantageinGame2fromGame1_playerB= self.CummuatedDisdvantageinGame2fromGame1_playerB + (
                                float(GameOutCome[1]) - float(GameOutCome[0]))
                        self.CummuatedDisdvantageinGame3fromGame1_playerB = self.CummuatedDisdvantageinGame3fromGame1_playerB + (
                                float(GameOutCome[1]) - float(GameOutCome[0]))

                    else:
                        self.competitiveDisadvantageToPlayerB_game1 = 0

                    print("Competitive disadvantage =", self.competitiveDisadvantageToPlayerA_game1,
                          self.competitiveDisadvantageToPlayerB_game1)
                    print("-----------------------------------------")

                    # cumulate competitive disadvantage

                    self.cummulatedCompetitiveDisadvantageToPlayerAGame1 = self.cummulatedCompetitiveDisadvantageToPlayerAGame1+self.competitiveDisadvantageToPlayerA_game1
                    self.cummulatedCompetitiveDisadvantageToPlayerBGame1 = self.cummulatedCompetitiveDisadvantageToPlayerBGame1 + self.competitiveDisadvantageToPlayerB_game1

                    # create matrices for additional costs

                    TotalCostAdditiontoA1 = np.array(
                        [[CostOfGame1CarriedForwardToNexRound, CostOfGame1CarriedForwardToNexRound],
                         [CostOfGame1CarriedForwardToNexRound, CostOfGame1CarriedForwardToNexRound]])

                    TotalCostAdditiontoB1 = np.array(
                        [[CostOfGame1CarriedForwardToNexRound, CostOfGame1CarriedForwardToNexRound],
                         [CostOfGame1CarriedForwardToNexRound, CostOfGame1CarriedForwardToNexRound]])

                    print("game 1", TotalCostAdditiontoA1, TotalCostAdditiontoB1)
                    print("A1", A1)
                    print("B1", B1)


                    self.TotalCostofPlayerAGame1 = self.TotalCostofPlayerAGame1 + GameOutCome[0]
                    self.TotalCostofPlayerBGame1 = self.TotalCostofPlayerBGame1 + GameOutCome[1]

                    self.TotalCostGame1 = self.TotalCostGame1 + CostofGame

                    self.CummulativeTotalCostGame1.append(self.TotalCostGame1)
                    self.ListOfProbOfA_game1.append(probofPlayerA)
                    self.ListOfProbOfB_game1.append(probofPlayerB)

                    print ("Prob Player A ", self.ListOfProbOfA_game1)
                    print ("Prob Player B ", self.ListOfProbOfB_game1)

                    self.CummualativeCostOfPlayerAGame1.append(self.TotalCostofPlayerAGame1)
                    self.CummualativeCostOfPlayerBGame1.append(self.TotalCostofPlayerBGame1)

                    #effect of games 2 and 3 total costs from game 1 result

                    self.CostIncreaseToGame2fromGame1 = self.CostIncreaseToGame2fromGame1 + float(
                        self.TotalGameCostCorrelation_1_to_2.get())*CostofGame
                    self.CostIncreaseToGame3fromGame1 = self.CostIncreaseToGame3fromGame1 + float(
                        self.TotalGameCostCorrelation_1_to_3.get()) * CostofGame

                if GameOrder[x] == 2:
                    # get probabilities of defecting for each player

                    # total cost impact from other games

                    TotalCostIncreaseToGame2 = self.CostIncreaseToGame2fromGame1 + self.CostIncreaseToGame2fromGame3

                    # total cost impact from other games

                    costToPlayerAMaxfromgames1and3 = (self.CummuatedDisdvantageinGame2fromGame1_playerA * float(self.CompetitiveCorrelation_1_to_2.get())) \
                                                     + (self.CummuatedDisdvantageinGame2fromGame3_playerA * float(self.CompetitiveCorrelation_3_to_2.get()))

                    costToPlayerBMaxfromgames1and3 = (self.CummuatedDisdvantageinGame2fromGame1_playerB * float(self.CompetitiveCorrelation_1_to_2.get())) \
                                                     + (self.CummuatedDisdvantageinGame2fromGame3_playerB * float(self.CompetitiveCorrelation_3_to_2.get()))


                    probofPlayerA = self.CaclculateNewProbabilityBasedOnTotaCost(Prob_of_A_defecting2,
                                                                                 float(self.Maximum_Survivable_game_cost_game2.get()),
                                                                                 self.TotalCostGame2 + self.cummulatedCompetitiveDisadvantageToPlayerAGame2
                                                                                 + TotalCostIncreaseToGame2 + costToPlayerAMaxfromgames1and3)


                    probofPlayerB = self.CaclculateNewProbabilityBasedOnTotaCost(Prob_of_B_defecting2,
                                                                                 float(self.Maximum_Survivable_game_cost_game2.get()),
                                                                                 self.TotalCostGame2+self.cummulatedCompetitiveDisadvantageToPlayerBGame2
                                                                                 + TotalCostIncreaseToGame2 + costToPlayerBMaxfromgames1and3)


                    playerStatus = self.determineIfAorBDefect(probofPlayerA, probofPlayerB)
                    print('Game number =', GameOrder[x], "=", playerStatus)
                    PlayerAStatusGame2 = playerStatus[0]
                    PlayerBStatusGame2 = playerStatus[1]

                    GameOutCome = self.DetermineCosts(PlayerAStatusGame2, PlayerBStatusGame2, self.A2_active, self.B2_active)
                    print(GameOutCome)
                    print("A2 Active = ", self.A2_active)
                    print("B2 Active = ", self.B2_active)
                    fractionCarriedForward = float(self.Fraction_of_cost_carried_forward_to_next_round_game2.get())
                    CostofGame = float(GameOutCome[0]) + float(GameOutCome[1])
                    CostOfGame2CarriedForwardToNexRound = fractionCarriedForward * CostofGame / 2

                    # determine competitive disadvantage

                    # for player A

                    # find out if A has co-operated and B defected

                    if playerStatus[0] == False and playerStatus[1] == True:
                        print("A has co-operated and B defected", playerStatus[0], playerStatus[1])
                        self.competitiveDisadvantageToPlayerA_game2 = float(self.Include_competitive_disadvantage_in_analysis_game2.get()) * (
                                    float(GameOutCome[0]) - float(GameOutCome[1]))

                        # effect on player A's position in games 1 and 3

                        self.CummuatedDisdvantageinGame1fromGame2_playerA = self.CummuatedDisdvantageinGame1fromGame2_playerA + (
                                float(GameOutCome[0]) - float(GameOutCome[1]))
                        self.CummuatedDisdvantageinGame3fromGame2_playerA = self.CummuatedDisdvantageinGame3fromGame2_playerA + (
                                float(GameOutCome[0]) - float(GameOutCome[1]))

                    else:
                        self.competitiveDisadvantageToPlayerA_game2 = 0

                    # for player B

                    # find out if B has co-operated and A defected

                    if playerStatus[1] == False and playerStatus[0] == True:
                        self.competitiveDisadvantageToPlayerB_game2 = float(self.Include_competitive_disadvantage_in_analysis_game2.get()) * (
                                    float(GameOutCome[1]) - float(GameOutCome[0]))

                        # effect on player B's position in games 1 and 3

                        self.CummuatedDisdvantageinGame1fromGame2_playerB = self.CummuatedDisdvantageinGame1fromGame2_playerB + (
                                float(GameOutCome[1]) - float(GameOutCome[0]))
                        self.CummuatedDisdvantageinGame3fromGame2_playerB = self.CummuatedDisdvantageinGame3fromGame2_playerB + (
                                float(GameOutCome[1]) - float(GameOutCome[0]))
                    else:
                        self.competitiveDisadvantageToPlayerB_game2 = 0

                    print("Competitive disadvantage =", self.competitiveDisadvantageToPlayerA_game2,
                          self.competitiveDisadvantageToPlayerB_game2)
                    print("-----------------------------------------")

                    # cumulate competitive disadvantage

                    self.cummulatedCompetitiveDisadvantageToPlayerAGame2 = self.cummulatedCompetitiveDisadvantageToPlayerAGame2 + self.competitiveDisadvantageToPlayerA_game2
                    self.cummulatedCompetitiveDisadvantageToPlayerBGame2 = self.cummulatedCompetitiveDisadvantageToPlayerBGame2 + self.competitiveDisadvantageToPlayerB_game2

                    # create matrices for additional costs

                    TotalCostAdditiontoA3 = np.array(
                        [[CostOfGame2CarriedForwardToNexRound, CostOfGame2CarriedForwardToNexRound],
                         [CostOfGame2CarriedForwardToNexRound + self.competitiveDisadvantageToPlayerA_game2, CostOfGame2CarriedForwardToNexRound]])

                    TotalCostAdditiontoB3 = np.array(
                        [[CostOfGame2CarriedForwardToNexRound, CostOfGame2CarriedForwardToNexRound + self.competitiveDisadvantageToPlayerB_game2],
                         [CostOfGame2CarriedForwardToNexRound, CostOfGame2CarriedForwardToNexRound]])

                    print("game 2", TotalCostAdditiontoA3, TotalCostAdditiontoB3)
                    print("A3", A3)
                    print("B3", B3)



                    self.TotalCostofPlayerAGame2 = self.TotalCostofPlayerAGame2 + GameOutCome[0]
                    self.TotalCostofPlayerBGame2 = self.TotalCostofPlayerBGame2 + GameOutCome[1]

                    self.TotalCostGame2 = self.TotalCostGame2 + CostofGame
                    self.CummulativeTotalCostGame2.append(self.TotalCostGame2)
                    self.ListOfProbOfA_game2.append(probofPlayerA)
                    self.ListOfProbOfB_game2.append(probofPlayerB)
                    self.CummualativeCostOfPlayerAGame2.append(self.TotalCostofPlayerAGame2)
                    self.CummualativeCostOfPlayerBGame2.append(self.TotalCostofPlayerBGame2)

                    #self.updateGameMatricesBasedOnPreviousGame(GameOrder[1], GameOrder[0], CostofGame)
                    #self.updateGameMatricesBasedOnPreviousGame(GameOrder[1], GameOrder[2], CostofGame)

                    self.CostIncreaseToGame1fromGame2 = self.CostIncreaseToGame1fromGame2 + float(
                        self.TotalGameCostCorrelation_2_to_1.get()) * CostofGame
                    self.CostIncreaseToGame3fromGame2 = self.CostIncreaseToGame3fromGame2 + float(
                        self.TotalGameCostCorrelation_2_to_3.get()) * CostofGame

                if GameOrder[x] == 3:

                    # total cost impact from other games

                    TotalCostIncreaseToGame3 = self.CostIncreaseToGame3fromGame1 + self.CostIncreaseToGame3fromGame2

                    # total cost impact from other games

                    costToPlayerAMaxfromgames1and2 = (self.CummuatedDisdvantageinGame3fromGame1_playerA * float(self.CompetitiveCorrelation_1_to_3.get())) \
                                                     + (self.CummuatedDisdvantageinGame3fromGame2_playerA * float(self.CompetitiveCorrelation_2_to_3.get()))

                    costToPlayerBMaxfromgames1and2 = (self.CummuatedDisdvantageinGame2fromGame1_playerB * float(self.CompetitiveCorrelation_1_to_2.get())) \
                                                     + (self.CummuatedDisdvantageinGame2fromGame3_playerB * float(self.CompetitiveCorrelation_3_to_2.get()))

                    probofPlayerA = self.CaclculateNewProbabilityBasedOnTotaCost(Prob_of_A_defecting3,
                                                                                 float(self.Maximum_Survivable_game_cost_game3.get()),
                                                                                 self.TotalCostGame3 + self.cummulatedCompetitiveDisadvantageToPlayerAGame3
                                                                                 + TotalCostIncreaseToGame3 + costToPlayerAMaxfromgames1and2)


                    probofPlayerB = self.CaclculateNewProbabilityBasedOnTotaCost(Prob_of_B_defecting3,
                                                                                 float(self.Maximum_Survivable_game_cost_game3.get()),
                                                                                 self.TotalCostGame3 + self.cummulatedCompetitiveDisadvantageToPlayerBGame3
                                                                                 + TotalCostIncreaseToGame3 + costToPlayerBMaxfromgames1and2)

                    playerStatus = self.determineIfAorBDefect(probofPlayerA, probofPlayerB)
                    print('Game number =', GameOrder[x], "=", playerStatus)
                    PlayerAStatusGame3 = playerStatus[0]
                    PlayerBStatusGame3 = playerStatus[1]

                    GameOutCome = self.DetermineCosts(PlayerAStatusGame3, PlayerBStatusGame3, self.A3_active, self.B3_active)
                    print(GameOutCome)
                    print("A3 Active = ", self.A3_active)
                    print("B3 Active = ", self.B3_active)
                    fractionCarriedForward = float(self.Fraction_of_cost_carried_forward_to_next_round_game3.get())
                    CostofGame = float(GameOutCome[0]) + float(GameOutCome[1])
                    CostOfGame3CarriedForwardToNexRound = fractionCarriedForward * CostofGame / 2

                    # determine competitive disadvantage

                    # for player A

                    # find out if A has co-operated and B defected

                    if playerStatus[0] == False and playerStatus[1] == True:
                        print("A has co-operated and B defected", playerStatus[0], playerStatus[1])
                        self.competitiveDisadvantageToPlayerA_game3 = float(self.Include_competitive_disadvantage_in_analysis_game3.get()) * (
                                    float(GameOutCome[0]) - float(GameOutCome[1]))

                        # effect on player A's position in games 1 and 2

                        self.CummuatedDisdvantageinGame1fromGame3_playerA = self.CummuatedDisdvantageinGame1fromGame3_playerA + (
                                float(GameOutCome[0]) - float(GameOutCome[1]))
                        self.CummuatedDisdvantageinGame2fromGame3_playerA = self.CummuatedDisdvantageinGame2fromGame3_playerA + (
                                float(GameOutCome[0]) - float(GameOutCome[1]))
                    else:
                        self.competitiveDisadvantageToPlayerA_game3 = 0

                    # for player B

                    # find out if B has co-operated and A defected

                    if playerStatus[1] == False and playerStatus[0] == True:
                        self.competitiveDisadvantageToPlayerB_game3 = float(self.Include_competitive_disadvantage_in_analysis_game3.get()) * (
                                    float(GameOutCome[1]) - float(GameOutCome[0]))

                        # effect on player B's position in games 1 and 3

                        self.CummuatedDisdvantageinGame1fromGame3_playerB = self.CummuatedDisdvantageinGame1fromGame3_playerB + (
                                float(GameOutCome[1]) - float(GameOutCome[0]))
                        self.CummuatedDisdvantageinGame2fromGame3_playerB = self.CummuatedDisdvantageinGame2fromGame3_playerB + (
                                float(GameOutCome[1]) - float(GameOutCome[0]))
                    else:
                        self.competitiveDisadvantageToPlayerB_game3 = 0

                    print("Competitive disadvantage =", self.competitiveDisadvantageToPlayerA_game3,
                          self.competitiveDisadvantageToPlayerB_game3)
                    print("-----------------------------------------")

                    # cumulate competitive disadvantage

                    self.cummulatedCompetitiveDisadvantageToPlayerAGame3 = self.cummulatedCompetitiveDisadvantageToPlayerAGame3 + self.competitiveDisadvantageToPlayerA_game3
                    self.cummulatedCompetitiveDisadvantageToPlayerBGame3 = self.cummulatedCompetitiveDisadvantageToPlayerBGame3 + self.competitiveDisadvantageToPlayerB_game3

                    # create matrices for additional costs

                    TotalCostAdditiontoA3 = np.array(
                        [[CostOfGame3CarriedForwardToNexRound, CostOfGame3CarriedForwardToNexRound],
                         [CostOfGame3CarriedForwardToNexRound + self.competitiveDisadvantageToPlayerA_game3, CostOfGame3CarriedForwardToNexRound]])

                    TotalCostAdditiontoB3 = np.array(
                        [[CostOfGame3CarriedForwardToNexRound, CostOfGame3CarriedForwardToNexRound + self.competitiveDisadvantageToPlayerB_game3],
                         [CostOfGame3CarriedForwardToNexRound, CostOfGame3CarriedForwardToNexRound]])

                    print("game 3", TotalCostAdditiontoA3, TotalCostAdditiontoB3)
                    print("A3", A3)
                    print("B3", B3)



                    self.TotalCostofPlayerAGame3 = self.TotalCostofPlayerAGame3 + GameOutCome[0]
                    self.TotalCostofPlayerBGame3 = self.TotalCostofPlayerBGame3 + GameOutCome[1]

                    self.TotalCostGame3 = self.TotalCostGame3 + CostofGame
                    self.CummulativeTotalCostGame3.append(self.TotalCostGame3)
                    self.ListOfProbOfA_game3.append(probofPlayerA)
                    self.ListOfProbOfB_game3.append(probofPlayerB)
                    self.CummualativeCostOfPlayerAGame3.append(self.TotalCostofPlayerAGame3)
                    self.CummualativeCostOfPlayerBGame3.append(self.TotalCostofPlayerBGame3)

                    #self.updateGameMatricesBasedOnPreviousGame(GameOrder[2], GameOrder[0], CostofGame)
                    #self.updateGameMatricesBasedOnPreviousGame(GameOrder[2], GameOrder[1], CostofGame)

                    self.CostIncreaseToGame1fromGame3 = self.CostIncreaseToGame1fromGame3 + float(
                        self.TotalGameCostCorrelation_3_to_1.get()) * CostofGame
                    self.CostIncreaseToGame2fromGame3 = self.CostIncreaseToGame2fromGame3 + float(
                        self.TotalGameCostCorrelation_3_to_2.get()) * CostofGame

            self.NumberOfRounds.append(counter)

            counter += 1

        LoopStatusComplete = True

        self.PlotGraphs()
        return LoopStatusComplete
        #plotgraphs

class plotgraphs:
    def __init__(self, master3):
        self.myFrame3 = Frame(master3)
        self.myFrame3.pack()
        plotgraphs.plotgraph(self)

        #GameSetUp.datasetup(self)

    def plotgraph(self):
        print(" we can plot graph here")

        self.Output = tkinter.LabelFrame(self.myFrame3, text="Outputs")
        self.Output.grid(row=0, column=0)

        # Plot graphs for game 1
        # total costs
        fig = Figure(figsize=(3, 2), dpi=100)
        fig.add_subplot(111).plot([1,2,3], [1,2,3])
        #textstg = "Max cost = " + str(self.TotalCostGame1)
        #fig.text(0.5, 0.8, textstg, horizontalalignment='center', verticalalignment='center')
        fig.suptitle("Total Costs Game 1")

        # plt.ylabel('Total cost of the game')
        # plt.xlabel("Negotiating Round")
        # plt.title("Total Cost")

        canvas = FigureCanvasTkAgg(fig, master=self.Output)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0)



Game = GameSetUp(root, root2)  # passes the root window to the class


root.mainloop()
