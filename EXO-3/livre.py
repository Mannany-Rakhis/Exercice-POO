class Livre:
    def __init__(self, titre, auteur, isbn, nb_pages, disponible=True):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.nb_pages = nb_pages
        self.disponible = disponible 
        
        
        
        def afficher(self):
           print(f"Titre: {self.titre}")
           print(f"Auteur: {self.auteur}")
           print(f"ISBN: {self.isbn}")
           print(f"Nombre de pages: {self.nb_pages}")
           print(f"Disponible: {self.disponible}") 
        
        
        def emprunter(self, nom_emprunteur):
            if self.disponible:
                self.disponible = False
                self.emprunteur = nom_emprunteur
                print(f"Le livre '{self.titre}' a été emprunté par {nom_emprunteur}")
            else:
                print(f"Le livre '{self.titre}' n'est pas disponible")
                
        def rendre(self):
            if not self.disponible:
                    self.disponible = True
                    self.emprunteur = None
                    print(f"Le livre '{self.titre}' a été rendu")
            else:
                    print(f"Le livre '{self.titre}' n'a pas été emprunté")
                
        def temps_lecture_estime(self):
                    return self.nb_pages