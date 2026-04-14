class Livre:
    def __init__(self, titre, auteur, isbn, nb_pages):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.nb_pages = nb_pages
        self.disponible = True
        self.emprunteur = None

    def afficher(self):
        statut = "Disponible" if self.disponible else f"Emprunté par {self.emprunteur}"
        print(f"'{self.titre}' de {self.auteur} ({self.nb_pages} pages) — {statut}")

    def emprunter(self, nom_emprunteur):
        if self.disponible:
            self.disponible = False
            self.emprunteur = nom_emprunteur
            print(f"Le livre '{self.titre}' a été emprunté par {nom_emprunteur}.")
        else:
            print(f"Le livre '{self.titre}' n'est pas disponible.")

    def rendre(self):
        if not self.disponible:
            self.disponible = True
            self.emprunteur = None
            print(f"Le livre '{self.titre}' a été rendu.")
        else:
            print(f"Le livre '{self.titre}' n'était pas emprunté.")

    def temps_lecture_estime(self):
        return self.nb_pages  

