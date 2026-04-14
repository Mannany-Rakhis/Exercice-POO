class Voiture:
    nb_voitures = 0

    def __init__(self, marque, modele, annee, kilometrage, prix_neuf):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
        self.prix_neuf = prix_neuf
        Voiture.nb_voitures += 1
    
    def afficher(self):
        print(f"Marque: {self.marque}")
        print(f"Modèle: {self.modele}")
        print(f"Année: {self.annee}")
        print(f"Kilométrage: {self.kilometrage} km")
        print(f"Prix neuf: {self.prix_neuf} €")

    def est_recente(self):
        return self.annee >= 2020

    def parcourir(self, distance):
        self.kilometrage += distance

    def estimer_valeur(self):
        valeur = self.prix_neuf - 0.05 * self.kilometrage
        return max(valeur, 500)