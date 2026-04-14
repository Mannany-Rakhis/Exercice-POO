class CompteBancaire:
    taux_interet = 0.02 

    def __init__(self, titulaire, solde, decouvert_autorise=0):
        self.titulaire = titulaire
        self.solde = solde
        self.decouvert_autorise = decouvert_autorise
        self.historique = [] 

    def deposer(self, montant):
        """Ajoute le montant au solde et enregistre l'opération dans l'historique."""
        self.solde += montant
        self.historique.append(f"Dépôt de {montant}€")

    def retirer(self, montant):
        """Retire le montant du solde si possible, sinon affiche 'Opération refusée'.
        Enregistre dans l'historique uniquement si l'opération réussit."""
        if self.solde - montant >= -self.decouvert_autorise:
            self.solde -= montant
            self.historique.append(f"Retrait de {montant}€")
            return True
        else:
            print("Opération refusée")
            return False

    def virement(self, autre_compte, montant):
        """Effectue un virement vers un autre compte."""
        if self.retirer(montant):
            autre_compte.deposer(montant)
            self.historique.append(f"Virement de {montant}€ vers {autre_compte.titulaire}")
            autre_compte.historique.append(f"Virement de {montant}€ depuis {self.titulaire}")

    def afficher_historique(self):
        """Affiche toutes les opérations de l'historique."""
        print(f"Historique du compte de {self.titulaire} :")
        for operation in self.historique:
            print(f"  - {operation}")

    def appliquer_interets(self):
        """Applique les intérêts si le solde est positif."""
        if self.solde > 0:
            interets = self.solde * CompteBancaire.taux_interet
            self.solde += interets
            self.historique.append(f"Intérêts appliqués : +{interets:.2f}€")