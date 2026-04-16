class Produit:
    tva = 20

    def __init__(self, reference, nom, prix_ht):
        self._reference = reference
        self._nom       = nom
        self._prix_ht   = prix_ht

    def __str__(self):
        return f"{self._nom} ({self._reference}) - {self._prix_ht}€ HT"

    def __repr__(self):
        return f"Produit('{self._reference}', '{self._nom}', {self._prix_ht})"

    def __eq__(self, other):
        if not isinstance(other, Produit): return False
        return self._reference == other._reference

    def __hash__(self):
        return hash(self._reference)

    def __lt__(self, other):
        return self._prix_ht < other._prix_ht

    @classmethod
    def from_dict(cls, data):
        return cls(data["ref"], data["nom"], data["prix"])
 
    @staticmethod
    def valider_prix(prix):
        if isinstance(prix, bool): return False
        return isinstance(prix, (int, float)) and prix > 0                                                                                                                                                             