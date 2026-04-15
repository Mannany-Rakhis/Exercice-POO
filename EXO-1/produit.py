from abc import ABC, abstractmethod

class Produit(ABC):
    tva = 20

    def __init__(self, reference, nom, prix_ht, stock):
        self.reference = reference
        self.nom       = nom
        self.prix_ht   = prix_ht
        self.stock     = stock

    @abstractmethod
    def calculer_frais_livraison(self): pass

    @abstractmethod
    def afficher_details(self): pass

    def afficher(self):
        print(f"[{self.reference}] {self.nom} - {self.prix_ht}€ HT")

    @property
    def prix_ttc(self):
        return round(self.prix_ht * (1 + Produit.tva / 100), 2)