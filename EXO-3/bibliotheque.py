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

    def emprunter_livre(self, titre, nom_emprunteur):
        livre = self.rechercher(titre)
        if livre:
            if livre.disponible:
                livre.emprunter(nom_emprunteur)
                self.nb_emprunts_total += 1
            else:
                print(f"Le livre '{titre}' n'est pas disponible pour emprunt.")
        else:
            print(f"Le livre '{titre}' n'existe pas dans la bibliothèque.")


    def rendre_livre(self, titre):
        livre = self.rechercher(titre)
        if livre:
            if not livre.disponible:
                livre.rendre()
            else:
                print(f"Le livre '{titre}' n'a pas été emprunté.")
        else:
            print(f"Le livre '{titre}' n'existe pas dans la bibliothèque.")
    
    def statistiques(self):
        print(f"Nombre total de livres : {len(self.livres)}")
        print(f"Nombre de livres disponibles : {len(self.livres_disponibles())}")
        print(f"Nombre total d'emprunts : {self.nb_emprunts_total}")
        
    def livres_disponibles(self):
        return [livre for livre in self.livres if livre.disponible]
    