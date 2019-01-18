# coding: utf-8
import requests

class GeneralController:

    def __init__(self, requete):
        self.requete = requete

    def checkRequete(self):
        if self.requete == 1:
            print("case 1")
            url = 'http://127.0.0.1:5001/restapi/compute/cvim1/new_vnf'
            data = '{"image":"ubuntu:trusty", "network":"(id=input,ip=10.0.0.1/24),(id=output,ip=20.0.0.1/24)"}'
            requests.put(url, data=data)
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