class Temperature:
    def __init__(self, valeur_celsius):
        """
        Initialise une température en Celsius.
        Valide que la valeur est un nombre (pas booléen) et dans [-273.15, 1_000_000].
        """
        if isinstance(valeur_celsius, bool):
            raise TypeError("Pas de booléen pour la température")
        if not isinstance(valeur_celsius, (int, float)):
            raise TypeError("La température doit être un nombre")
        if valeur_celsius < -273.15:
            raise ValueError("Température inférieure au zéro absolu (-273.15°C)")
        if valeur_celsius > 1_000_000:
            raise ValueError("Température trop élevée (max : 1 000 000°C)")
        self._valeur_celsius = valeur_celsius

    @property
    def valeur_celsius(self):
        return self._valeur_celsius

    @valeur_celsius.setter
    def valeur_celsius(self, valeur):
        if isinstance(valeur, bool):
            raise TypeError("Pas de booléen pour la température")
        if not isinstance(valeur, (int, float)):
            raise TypeError("La température doit être un nombre")
        if valeur < -273.15:
            raise ValueError("Température inférieure au zéro absolu (-273.15°C)")
        if valeur > 1_000_000:
            raise ValueError("Température trop élevée (max : 1 000 000°C)")
        self._valeur_celsius = valeur


    @property
    def fahrenheit(self):
        """Convertit en Fahrenheit : F = (C × 9/5) + 32"""
        return round((self._valeur_celsius * 9 / 5) + 32, 2)

    @property
    def kelvin(self):
        """Convertit en Kelvin : K = C + 273.15"""
        return round(self._valeur_celsius + 273.15, 2)

    @property
    def etat(self):
        """Retourne l'état de l'eau à cette température."""
        if self._valeur_celsius <= 0:
            return "solide"
        elif self._valeur_celsius < 100:
            return "liquide"
        else:
            return "gazeux"


    @classmethod
    def depuis_fahrenheit(cls, valeur_f):
        """
        Crée un objet Temperature à partir d'une valeur en Fahrenheit.
        Formule : C = (F - 32) * 5/9
        """
        celsius = (valeur_f - 32) * 5 / 9
        return cls(celsius)


    def est_compatible_avec(self, autre):
        """
        Retourne True si les deux températures ont le même état de l'eau.
        """
        if not isinstance(autre, Temperature):
            raise TypeError("L'argument doit être un objet Temperature")
        return self.etat == autre.etat