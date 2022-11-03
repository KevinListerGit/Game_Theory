import tkinter
import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


root = tkinter.Tk()
root.title("trajectory")
root.geometry("1600x800")

class GameSetUp:
    def __init__(self,master):
        self.myFrame = Frame(master)
        self.myFrame.pack()

        # data set up

        self.Data_set_up = tkinter.LabelFrame(self.myFrame, text="Data Set Up")
        self.Data_set_up.grid(row=0, column=0)

        #probability set up

        self.Probability_set_up = tkinter.LabelFrame(self.Data_set_up, text="Probability Set Up")
        self.Probability_set_up.grid(row=0, column=0, padx=50, pady=10)

        self.Probability_of_PlayerA_defecting_label = tkinter.Label(self.Probability_set_up, text="Probability of A defecting")
        self.Probability_of_PlayerA_defecting_label.grid(row=0, column=0)

        self.Probability_of_PlayerB_defecting_label = tkinter.Label(self.Probability_set_up, text="Probability of B defecting")
        self.Probability_of_PlayerB_defecting_label.grid(row=1, column=0)

        self.Probability_of_PlayerA_defecting = tkinter.Entry(self.Probability_set_up)
        self.Probability_of_PlayerA_defecting.grid(row=0, column=1)

        self.Probability_of_PlayerB_defecting = tkinter.Entry(self.Probability_set_up)
        self.Probability_of_PlayerB_defecting.grid(row=1, column=1)

        # game set up data

        self.Game_parameters = tkinter.LabelFrame(self.Data_set_up, text="Game Parameters")
        self.Game_parameters.grid(row=0, column=1)

        self.Maximum_Survivable_game_cost_label = tkinter.Label(self.Game_parameters, text="Maximum Survivable Cost ")
        self.Maximum_Survivable_game_cost_label.grid(row=0, column=0, padx=50)

        self.Maximum_Survivable_game_cost = tkinter.Entry(self.Game_parameters)
        self.Maximum_Survivable_game_cost.grid(row=0, column=1)

        self.Fraction_of_cost_carried_forward_to_next_round_label = tkinter.Label(self.Game_parameters,
                                                                             text="Fraction game total carried forward to next round")
        self.Fraction_of_cost_carried_forward_to_next_round_label.grid(row=1, column=0)

        self.Fraction_of_cost_carried_forward_to_next_round = tkinter.Entry(self.Game_parameters)
        self.Fraction_of_cost_carried_forward_to_next_round.grid(row=1, column=1)

        self.Fraction_of_competitive_disadvantage_label = tkinter.Label(self.Game_parameters,
                                                                   text="Fraction of competitive disadvantage added to max cost")
        self.Fraction_of_competitive_disadvantage_label.grid(row=3, column=0)

        self.Fraction_of_competitive_disadvantage = tkinter.Entry(self.Game_parameters)
        self.Fraction_of_competitive_disadvantage.grid(row=3, column=1)

        self.Number_of_rounds_label = tkinter.Label(self.Game_parameters, text="Number of rounds")
        self.Number_of_rounds_label.grid(row=4, column=0)

        self.Number_of_rounds = tkinter.Entry(self.Game_parameters)
        self.Number_of_rounds.grid(row=4, column=1)

        # matrix data input

        self.Matrix = tkinter.LabelFrame(self.myFrame, text="Cost Set Up")
        self.Matrix.grid(row=1, column=0, padx=20, pady=20)

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

        self.PlayerADefectCostIfPlayerBDefects = tkinter.Entry(self.Cell_11)
        self.PlayerADefectCostIfPlayerBDefects.grid(row=0, column=0)

        self.PlayerBDefectCostIfPlayerADefects = tkinter.Entry(self.Cell_11)
        self.PlayerBDefectCostIfPlayerADefects.grid(row=0, column=1)

        self.Cell_21 = tkinter.LabelFrame(self.Matrix)
        self.Cell_21.grid(row=2, column=2)

        self.PlayerADefectCostIfPlayerBCooperates = tkinter.Entry(self.Cell_21)
        self.PlayerADefectCostIfPlayerBCooperates.grid(row=0, column=0)

        self.PlayerBCooperatesCostIfPlayerADefects = tkinter.Entry(self.Cell_21)
        self.PlayerBCooperatesCostIfPlayerADefects.grid(row=0, column=1)

        self.Cell_12 = tkinter.LabelFrame(self.Matrix)
        self.Cell_12.grid(row=3, column=1)

        self.PlayerACooperatesCostIfPlayerBDefects = tkinter.Entry(self.Cell_12)
        self.PlayerACooperatesCostIfPlayerBDefects.grid(row=0, column=0)

        self.PlayerBDefectsCostIfPlayerACooperates = tkinter.Entry(self.Cell_12)
        self.PlayerBDefectsCostIfPlayerACooperates.grid(row=0, column=1)

        self.Cell_22 = tkinter.LabelFrame(self.Matrix)
        self.Cell_22.grid(row=3, column=2)

        self.PlayerACooperatesCostIfPlayerBCooperates = tkinter.Entry(self.Cell_22)
        self.PlayerACooperatesCostIfPlayerBCooperates.grid(row=0, column=0)

        self.PlayerBCooperatesCostIfPlayerACooperates = tkinter.Entry(self.Cell_22)
        self.PlayerBCooperatesCostIfPlayerACooperates.grid(row=0, column=1)

        self.Data_entry_button = tkinter.Button(self.myFrame, text="Commence analysis", command=self.analyse)
        self.Data_entry_button.grid(row=2, column=0)





    def analyse(self):
        Prob_of_A_defecting = float(self.Probability_of_PlayerA_defecting.get())
        Prob_of_B_defecting = float(self.Probability_of_PlayerB_defecting.get())

        # Max_loss = input("Max Loss = ") Loss = ")
        # Pareto_opti
        # Min_loss = input("Minmum = input("Pareto_optimum = ")
        # Nash_equilibrium = input("Nash equilibrium = ")

        CostToA_ADefectwithBdefect = float(self.PlayerADefectCostIfPlayerBDefects.get())
        CostToB_BDefectwithAdefect = float(self.PlayerBDefectCostIfPlayerADefects.get())
        CostToA_ADefectwithBCooperation = float(self.PlayerADefectCostIfPlayerBCooperates.get())
        CostToB_BCooperateswithADefects = float(self.PlayerBCooperatesCostIfPlayerADefects.get())
        CostToA_ACooperateswithBdefect = float(self.PlayerACooperatesCostIfPlayerBDefects.get())
        CostToB_BDefectwithACooperates = float(self.PlayerBDefectsCostIfPlayerACooperates.get())
        CostToA_ACooperateswithBCooperates = float(self.PlayerACooperatesCostIfPlayerBCooperates.get())
        CostToB_BCooperateswithACooperates = float(self.PlayerBCooperatesCostIfPlayerACooperates.get())

        counter = 1

        Prob_of_A_defecting_new = Prob_of_A_defecting
        Prob_of_B_defecting_new = Prob_of_A_defecting


        # probabilities passed by function.
        #Prob_of_A_defecting = ProbOfADeftect
        #Prob_of_B_defecting = ProbOfBDefect

        # the matrix is (r,c), the first term is the row player and the second is the column player
        # separate payoff matrices for each player
        A = np.array([[CostToA_ADefectwithBdefect, CostToA_ADefectwithBCooperation],
                      [CostToA_ACooperateswithBdefect, CostToA_ACooperateswithBCooperates]])
        B = np.array([[CostToB_BDefectwithAdefect, CostToB_BCooperateswithADefects],
                      [CostToB_BDefectwithACooperates, CostToB_BCooperateswithACooperates]])

        # Set various variables used in the loops below to zero
        Change_to_pay_off_matrix = float(0)
        self.Cumulative_total_cost = []
        self.Cumulative_Cost_A = []  # list to store the cumulative costs for player A
        self.Cumulative_Cost_B = []  # list to store the cumulative costs for player B
        self.Round_number = []
        self.Prob_of_A_values = []
        self.Prob_of_B_values = []
        Competitive_disadvantage_A = float(0)
        Competitive_disadvantage_B = float(0)

        while counter < int(self.Number_of_rounds.get()):

            # the matrix is (r,c), the first term is the row player and the second is the column player
            # separate payoff matrices for each player
            A = np.array([[CostToA_ADefectwithBdefect + Change_to_pay_off_matrix,
                           CostToA_ADefectwithBCooperation + Change_to_pay_off_matrix],
                          [CostToA_ACooperateswithBdefect + Change_to_pay_off_matrix + Competitive_disadvantage_A,
                           CostToA_ACooperateswithBCooperates + Change_to_pay_off_matrix]])
            B = np.array([[CostToB_BDefectwithAdefect + Change_to_pay_off_matrix,
                           CostToB_BCooperateswithADefects + Change_to_pay_off_matrix + Competitive_disadvantage_B],
                          [CostToB_BDefectwithACooperates + Change_to_pay_off_matrix,
                           CostToB_BCooperateswithACooperates + Change_to_pay_off_matrix]])

            print("A=", A)
            print(A[0, 0], A[0, 1])
            print(A[1, 0], A[1, 1])

            print("B=", B)
            print(B[0, 0], B[0, 1])
            print(B[1, 0], B[1, 1])

            # set default status of A and B

            A_defects = False
            B_defects = False

            A_defects_status = random.random()
            if A_defects_status <= Prob_of_A_defecting_new:
                A_defects = True
            print("A defects", A_defects)

            B_defects_status = random.random()
            if B_defects_status <= Prob_of_B_defecting_new:
                B_defects = True
            print("B defects", B_defects)

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
                    Competitive_disadvantage_B = (Cost_B - Cost_A) * float(
                        self.Fraction_of_competitive_disadvantage.get())

            # A co-operates and B defects
            elif A_defects == False:
                if B_defects == True:
                    Cost_A = A[1, 0]
                    Cost_B = B[1, 0]
                    Competitive_disadvantage_A = (Cost_A - Cost_B) * float(
                        self.Fraction_of_competitive_disadvantage.get())
                # A co-operates and B co-operates
                elif B_defects == False:
                    Cost_A = A[1, 1]
                    Cost_B = B[1, 1]

            # determine competitive disadvantage

            #if Cost_A > Cost_B:
            #    Competitive_disadvantage_A = (Cost_A - Cost_B) * float(self.Fraction_of_competitive_disadvantage.get())

            #else:
            #    Competitive_disadvantage_B = (Cost_B - Cost_A) * float(self.Fraction_of_competitive_disadvantage.get())

            # Calculate the cost of the game and costs carried forward
            print("Cost_A =", Cost_A)
            print("Cost_B =", Cost_B)
            Total_Game_Cost = Cost_A + Cost_B
            if Total_Game_Cost > float(self.Maximum_Survivable_game_cost.get()):
                break

            Cost_carried_forward = float(self.Fraction_of_cost_carried_forward_to_next_round.get()) * Total_Game_Cost
            Change_to_pay_off_matrix = Cost_carried_forward / 2  # Assume both players suffer carry an equal share of the Total Game Cost

            # Revise the probabilities of defecting based on the total game cost
            # It is assumed that once the total game cost is reached there is no incentive to co-operate so the
            # probability of defecting is 1

            Gradient_of_probability_line_playerA = (1-Prob_of_A_defecting) / (float(self.Maximum_Survivable_game_cost.get()))
            Prob_of_A_defecting_new = Gradient_of_probability_line_playerA * (
                        Total_Game_Cost + A[1, 0]) + Prob_of_A_defecting
            if Prob_of_A_defecting_new > 1:
                Prob_of_A_defecting_new = 1

            Gradient_of_probability_line_playerB = (1-Prob_of_B_defecting) / (float(self.Maximum_Survivable_game_cost.get()))
            Prob_of_B_defecting_new = Gradient_of_probability_line_playerB * (
                        Total_Game_Cost + B[
                    0, 1]) + Prob_of_B_defecting
            if Prob_of_B_defecting_new > 1:
                Prob_of_B_defecting_new = 1

            if Prob_of_A_defecting_new < 0:
                Prob_of_A_defecting_new = 0

            if Prob_of_B_defecting_new < 0:
                Prob_of_B_defecting_new = 0

            # record probabilities

            self.Prob_of_A_values.append(Prob_of_A_defecting_new)
            self.Prob_of_B_values.append(Prob_of_B_defecting_new)

            # record costs

            self.Cumulative_total_cost.append(Total_Game_Cost)
            self.Cumulative_Cost_A.append(Cost_A)
            self.Cumulative_Cost_B.append(Cost_B)
            self.Round_number.append(counter)
            counter += 1

            print("Total Game Cost = ", Total_Game_Cost)
            print("Cost Carried Forwards = ", Cost_carried_forward)
            print("change to payoff matrix = ", Change_to_pay_off_matrix)

        print(self.Cumulative_total_cost)

        # we not plot on the page
        #total costs first

        #self.Matrix = tkinter.LabelFrame(self.myFrame, text="Cost Set Up")
        #self.Matrix.grid(row=1, column=0, padx=20, pady=20)

        self.Output = tkinter.LabelFrame(self.myFrame, text="Outputs")
        self.Output.grid(row=3, column=0)

        fig = Figure(figsize=(5, 4), dpi=100)
        fig.add_subplot(111).plot(self.Round_number, self.Cumulative_total_cost)
        fig.suptitle("Total Costs")


        if counter < int(self.Number_of_rounds.get()):
            Text_for_graph = "All dead after " + str(counter) + " rounds"  # create text for string for graph
            #plt.text(1, 180, Text_for_graph, size=12, )
            fig.text(1, 1, Text_for_graph, size=12, )

        #plt.ylabel('Total cost of the game')
        #plt.xlabel("Negotiating Round")
        #plt.title("Total Cost")

        canvas = FigureCanvasTkAgg(fig, master=self.Output)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0)


        # cost per player for the second graph

        #self.Output = tkinter.LabelFrame(self.myFrame, text="Outputs")
        #self.Output.grid(row=3, column=1)

        fig = Figure(figsize=(5, 4), dpi=100)
        fig.add_subplot(111).plot(self.Round_number, self.Cumulative_Cost_A, self.Round_number, self.Cumulative_Cost_B, label="Player A")
        #fig.add_subplot(111).plot(self.Round_number, self.Cumulative_Cost_B, label="Player B")
        fig.suptitle("Player Costs")
        fig.legend([self.Cumulative_Cost_A, self.Cumulative_Cost_B],["Player A", "Player B"], loc="upper right")


        canvas = FigureCanvasTkAgg(fig, master=self.Output)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row= 0, column= 1)

        # plot probabilities of defecting on the third graph

        #self.Output = tkinter.LabelFrame(self.myFrame, text="Outputs")
        #self.Output.grid(row=3, column=1)

        fig = Figure(figsize=(5, 4), dpi=100)
        fig.add_subplot(111).plot(self.Round_number, self.Prob_of_A_values, self.Round_number, self.Prob_of_B_values,
                                  )
        # fig.add_subplot(111).plot(self.Round_number, self.Cumulative_Cost_B, label="Player B")
        fig.suptitle("Probabilities of Defecting")

        # plt.ylabel('Total cost of the game')
        # plt.xlabel("Negotiating Round")
        # plt.title("Total Cost")

        canvas = FigureCanvasTkAgg(fig, master=self.Output)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=2)



        # we now plot

        # plot of total costs

        #plt.plot(self.Round_number, self.Cumulative_total_cost)
        plt.ylabel('Total cost of the game')
        plt.xlabel("Negotiating Round")
        plt.title("Total Cost")
        if counter < int(self.Number_of_rounds.get()):
            Text_for_graph = "All dead after " + str(counter) + " rounds"  # create text for string for graph
            plt.text(1, 180, Text_for_graph, size=12, )  # add text string to graph
        #plt.show()

        # plot of player costs

        plt.plot(self.Round_number, self.Cumulative_Cost_A, label="Player A")
        plt.plot(self.Round_number, self.Cumulative_Cost_B, label="Player B")  # plt is the object and we call the method plot.
        plt.ylabel('Cumulative Cost Player A')
        plt.xlabel("Negotiating Round")
        plt.title("Costs for Player A and B")
        plt.legend(loc='best')
        # plt.text(1, 7, Text_for_graph, size=12, math_fontfamily='cm')  # add text string to graph

        #plt.show()

        # plot of probabilities
        plt.plot(self.Round_number, self.Prob_of_A_values, label="Player A")
        plt.plot(self.Round_number, self.Prob_of_B_values, label="Player B")  # plt is the object and we call the method plot.
        plt.ylabel('Prob of defecting')
        plt.xlabel("Negotiating Round")
        plt.title("Probabilities of defecting")
        plt.legend(loc="upper left", )

        #plt.show()




Game = GameSetUp(root) # passes the root window to the class

root.mainloop()

