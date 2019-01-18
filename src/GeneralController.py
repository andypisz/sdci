# coding: utf-8
import requests


class GeneralController:

    def __init__(self, requete, IHM):
        self.requete = requete
        self.IHM = IHM

    def checkRequete(self):
        if self.requete == 1:
            self.IHM.printMessage("Entrez le nom de la VNF que vous souhaitez ajouter :")
            vnf_name = self.IHM.askUserInputVnfName()
            url = 'http://127.0.0.1:5001/restapi/compute/dc1/' + vnf_name
            data = '{"image":"ubuntu:trusty", "network":"(id=input,ip=10.0.0.1/24),(id=output,ip=20.0.0.1/24)"}'
            requests.put(url, data=data)
        elif self.requete == 2:
            self.IHM.printMessage("Entrez le nom de la VNF que vous souhaitez supprimer :")
            vnf_name = self.IHM.askUserInputVnfName()
            url = 'http://127.0.0.1:5001/restapi/compute/dc1/' + vnf_name
            requests.delete(url)
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