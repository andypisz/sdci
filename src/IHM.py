# coding: utf-8

import Global
from GeneralController import GeneralController
import sys
import re


class IHM:

    def __init__(self):
        self.userInput = -1
        self.actions = Global.ACTIONS

    def printMenu(self):
        i = 0
        print("\nChoisissez une option en entrant le numéro correspondant :")
        print("==========================================================\n")
        for action in self.actions:
            print(str(i)+": "+action)
            i += 1

    def askUserInputMainMenu(self):
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
                    print("La valeur entrée est incorrecte, entrez un nombre entre 0 et "+str(len(self.actions))+".")
            except ValueError:
                print("La valeur entrée est incorrecte, entrez un nombre entre 0 et "+str(len(self.actions))+".")

    def askUserInputVnfName(self):
        input_correct = False
        while not input_correct:
            user_input = str(input())
            input_correct = re.match('^[\w-]+$', user_input) is not None
            if (input_correct):
                return user_input
            else:
                print("La valeur entrée est incorrecte, entrez un uniquement des caractères alphanumériques.")

    def printMessage(self, message):
        print(message)

    def printUserInput(self):
        print("Vous avez choisi : "+ str(self.userInput)+"\n")

    def getUserInput(self):
        return self.userInput

    def launchIHM(self):
        while(True):
            self.printMenu()
            self.askUserInputMainMenu()
            self.printUserInput()
            monGeneralController = GeneralController(self.userInput, self)
            monGeneralController.checkRequete()
