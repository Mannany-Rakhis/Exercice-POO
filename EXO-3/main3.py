from bibliotheque import Bibliotheque
from livre import Livre

if __name__ == "__main__":
    biblio = Bibliotheque("Bibliothèque Centrale")

    livre1 = Livre("1984", "George Orwell", "978-0451524935", 328)
    livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "978-0156013987", 96)
    biblio.ajouter_livre(livre1)
    biblio.ajouter_livre(livre2)

    biblio.emprunter_livre("1984", "Alice")
    biblio.emprunter_livre("Le Petit Prince", "Bob")

    biblio.statistiques()

    biblio.rendre_livre("1984")
    biblio.statistiques()