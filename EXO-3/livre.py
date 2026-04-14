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