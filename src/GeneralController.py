class GeneralController:

    def __init__(self, requete):
        self.requete = requete

    def checkRequete(self):
        if self.requete == 1:
            print("case 1")
        elif self.requete == 2:
            print("case 2")
        elif self.requete == 3:
            print("case 3")
        elif self.requete == 4:
            print("case 4")
        elif self.requete == 5:
            print("case 5")
        elif self.requete == 6:
            print("case 6")
        else:
            print("default")