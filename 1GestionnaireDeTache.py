import os



class Tableau:
    
    def __init__(self, nom):
        self.surface = ""
        self.fichier = open(nom+".txt", "a", encoding="utf-8")

        self.URGENTsurface=""
        self.NormalSurface=""
        self.NOTimpSurface=""
        self.UpdateSurface=""
        self.undefinedSurface=""
        self.OtherSurface=""

        self.nom = nom

    def ecrire(self, message,):
        self.fichier.write(message + "\n")
            
        self.surface += message + "\n"

    
    def ajouter(self, titre="Sans titre", prio="undefined", tache="Aucune Tache Definis", statut="Non_Terminee"):

        self.ecrire("\nTACHE: " + titre + ":\n")
        self.ecrire("Prioritee: " + prio)
        self.ecrire(tache)
        self.ecrire("Statut: " + statut + "\n")
        self.ecrire("-----------------------------")


    def trier(self):
        self.trie = self.surface.split("-----------------------------")
        for Task in self.trie:
            if "URGENT" in Task:
                self.URGENTsurface += Task +"-----------------------------"
            elif "Normal" in Task:
                self.NormalSurface += Task +"-----------------------------"
            elif "Not important" in Task:
                self.NOTimpSurface += Task +"-----------------------------"
            elif Task == "" or Task == "\n" or Task == " ":
                pass
            else:
                #print(Task + " \npriority not defined")
                self.undefinedSurface += Task +"-----------------------------"
            
        self.surface = ""
        self.fichier.truncate(0)
        self.ecrire(self.URGENTsurface)
        
        self.ecrire(self.NormalSurface)

        self.ecrire(self.NOTimpSurface)

        self.ecrire(self.undefinedSurface)
        
        

    def fait(self, TitreTache):
        self.faire = self.surface.split("-----------------------------")
        for Task in self.faire:
            if "TACHE: "+ TitreTache in Task:
                self.TaskList = Task.split(" ")
                for Mot in self.TaskList:
                    if "Non_Terminee" in Mot:
                        Mot = "Terminee"
                    else:
                        pass
                    self.UpdateSurface += Mot +" "
                self.UpdateSurface += "\n-----------------------------"
            else:
                self.UpdateSurface += Task + "\n-----------------------------"
        self.surface = ""                                                                             ############
        self.surface+= self.UpdateSurface 
        
        self.fichier.truncate(0)
        self.ecrire(self.surface)
        
        
        
        
        

    def effacer(self, NomTache):
        self.efface = self.surface.split("-----------------------------")
        for Task in self.efface:
            if "TACHE: "+ NomTache in Task:
                print("Task founded !")
                print("Task deleted")
            else:
                self.UpdateSurface += Task + "\n-----------------------------"
                print("this Task is not the task to earase")
        self.surface = ""
        self.surface+= self.UpdateSurface 
        
        self.fichier.truncate(0)
        self.ecrire(self.surface)

    def clear(self):
        self.fichier.truncate(0)

    def done(self):
        self.fichier.close()
        




tab = Tableau("Taches")
tab.clear()
tab.ajouter("Titre", "Prioritée", "Commentaire de la Tache")
tab.ajouter("Lire", "Normal", "LireMerlin")
tab.ajouter("Dormir","URGENT")
tab.ajouter("Manger")
tab.ajouter("Ecole", "Normal", "aller a l'ecole")
tab.effacer("Dormir")


tab.trier()

tab.fait("Lire")





tab.done()