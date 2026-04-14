class Livre:
    def __init__(self, titre, auteur, isbn, nb_pages, disponible=True):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.nb_pages = nb_pages
        self.disponible = disponible 