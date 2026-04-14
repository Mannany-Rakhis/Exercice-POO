class Bibliotheque:

   def __init__(self, nom):
    self.nom = nom
    self.livres = []

    self.nb_emprunts_total = 0

   def ajouter_livre(self, livre):
    self.livres.append(livre)

    def rechercher(self, titre):
       for livre in self.livres:
          if livre.titre == titre:
            return livre
    return None