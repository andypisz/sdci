# coding: utf-8

import Global
from GeneralController import GeneralController
import sys


class IHM:

    def __init__(self):
        self.userInput = -1
        self.actions = Global.ACTIONS

    def printMenu(self):
        i = 0
        print("\nChoisissez une option en entrant le numéro correspondant :")
        print("==========================================================\n")
        for action in self.actions:
            print(i, ": ", action)
            i += 1

    def askUserInput(self):
        input_correct = False
        while not input_correct:
            user_input = input()
            try:
                int_user_input = int(user_input)
                if int_user_input == 0:
                    print("Au revoir !")
                    sys.exit(0)
                elif 1 <= int_user_input <= len(self.actions):
                    self.userInput = int_user_input
                    input_correct = True
                else:
                    print("La valeur entrée est incorrecte, entrez un nombre entre 0 et ", len(self.actions), ".")
            except ValueError:
                print("La valeur entrée est incorrecte, entrez un nombre entre 0 et ", len(self.actions), ".")

    def printUserInput(self):
        print("Vous avez choisi : ", self.userInput,"\n")

    def getUserInput(self):
        return self.userInput

    def launchIHM(self):
        while(True):
            self.printMenu()
            self.askUserInput()
            self.printUserInput()
            monGeneralController = GeneralController(self.userInput)
            monGeneralController.checkRequete()
