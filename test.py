class Arcenciel:
    def __init__(self,couleurs):
        self.couleurs = couleurs
    
    def Afficher4couleurs(self):
        print("Les couleurs de l'arcenciel sont :" + str(self.couleurs))

nb_couleurs = 6
liste_couleurs = []
for i in range(nb_couleurs):
    couleurs = input("Les couleurs " + str(i+1) + " : ")
    liste_couleurs.append(Arcenciel(couleurs))
         
for coleurs in liste_couleurs:
    coleurs.Afficher4couleurs()
