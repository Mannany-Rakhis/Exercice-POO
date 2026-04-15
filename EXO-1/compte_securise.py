class CompteBancaire:
    taux_interet = 0.02

    def __init__(self, titulaire, solde, decouvert_autorise=0):
        self.decouvert_autorise = decouvert_autorise
        self.historique = []  
        self.titulaire = titulaire
        self.solde = solde

    @property
    def titulaire(self):
        return self._titulaire

    @titulaire.setter
    def titulaire(self, valeur):
        if not isinstance(valeur, str):
            raise TypeError("Le titulaire doit être une chaîne")
        if not valeur.strip():
            raise ValueError("Le titulaire ne peut pas être vide")
        self._titulaire = valeur.strip()

    @property
    def decouvert_autorise(self):
        return self._decouvert_autorise

    @decouvert_autorise.setter
    def decouvert_autorise(self, valeur):
        if isinstance(valeur, bool):
            raise TypeError("Pas de booléen pour le découvert")
        if not isinstance(valeur, (int, float)):
            raise TypeError("Le découvert doit être un nombre")
        if valeur < 0:
            raise ValueError("Le découvert autorisé doit être positif ou nul")
        self._decouvert_autorise = valeur

    @property
    def solde(self):
        return self._solde

    @solde.setter
    def solde(self, valeur):
        if isinstance(valeur, bool):
            raise TypeError("Pas de booléen pour le solde")
        if not isinstance(valeur, (int, float)):
            raise TypeError("Le solde doit être un nombre")
        if valeur < -self._decouvert_autorise:
            raise ValueError(
                f"Solde insuffisant — découvert max : {self._decouvert_autorise}€"
            )
        self._solde = round(valeur, 2)

    @property
    def est_a_decouvert(self):
        return self._solde < 0

    @property
    def nb_operations(self):
        return len(self.historique)

    def deposer(self, montant):
        """Dépose un montant valide sur le compte et enregistre l'opération."""
        if isinstance(montant, bool):
            raise TypeError("Pas de booléen pour le montant")
        if not isinstance(montant, (int, float)):
            raise TypeError("Le montant doit être un nombre")
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        self._solde = round(self._solde + montant, 2)
        self.historique.append(f"+ {montant} | solde : {self._solde}")
        print(f"Dépôt de {montant}. Nouveau solde : {self._solde}")

    def retirer(self, montant):
        """Retire un montant si possible, enregistre l'opération et retourne True/False."""
        if isinstance(montant, bool):
            raise TypeError("Pas de booléen pour le montant")
        if not isinstance(montant, (int, float)):
            raise TypeError("Le montant doit être un nombre")
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        if self._solde - montant < -self._decouvert_autorise:
            print("Opération refusée — découvert dépassé")
            return False
        self._solde = round(self._solde - montant, 2)
        self.historique.append(f"- {montant} | solde : {self._solde}")
        print(f"Retrait de {montant}. Nouveau solde : {self._solde}")
        return True

    def virement(self, autre_compte, montant):
        """Effectue un virement vers un autre compte."""
        if self.retirer(montant):
            autre_compte.deposer(montant)

    def afficher_historique(self):
        """Affiche l'historique des opérations réussies."""
        print(f"Historique de {self._titulaire} :")
        for operation in self.historique:
            print(f"  {operation}")

    def appliquer_interets(self):
        """Applique les intérêts si le solde est positif."""
        if self._solde > 0:
            interets = round(self._solde * CompteBancaire.taux_interet, 2)
            self._solde = round(self._solde + interets, 2)
            self.historique.append(f"+ {interets} | solde : {self._solde} (intérêts)")