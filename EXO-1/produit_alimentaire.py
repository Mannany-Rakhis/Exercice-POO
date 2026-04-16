from produit import Produit
from datetime import date

class ProduitAlimentaire(Produit):
    def __init__(self, reference, nom, prix_ht, stock, date_peremption):
        super().__init__(reference, nom, prix_ht, stock)  
        self.date_peremption = date_peremption

    @property
    def date_peremption(self):
        return self._date_peremption   

    @date_peremption.setter
    def date_peremption(self, valeur):
        if isinstance(valeur, date):              
            self._date_peremption = valeur
            return
        if not isinstance(valeur, str):
            raise TypeError("La date doit être une chaîne ISO (YYYY-MM-DD)")
        try:
            self._date_peremption = date.fromisoformat(valeur)
        except ValueError:
            raise ValueError(f"Format invalide : '{valeur}'. Attendu : YYYY-MM-DD")

    def est_perime(self):
        return self._date_peremption < date.today()

    def calculer_frais_livraison(self):
        return 15.00

    def afficher_details(self):
        statut = " PÉRIMÉ" if self.est_perime() else "OK"
        print(f"  Péremption : {self._date_peremption} [{statut}]")