from livre import Livre
from bibliotheque import Bibliotheque

bibliotheque = Bibliotheque("Bibliothèque centrale") 
livre1 = Livre("harry potter", "J. K. Rowling", " 2-07-054127-4", 240)
livre2 = Livre("le seigneur des anneaux", "J. R. R. Tolkien", " 2-07-054127-5", 1200)
livre3 = Livre("le petit prince", "Antoine de Saint-Exupéry", " 2-07-054127-6", 96)

bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
bibliotheque.ajouter_livre(livre3)
bibliotheque.statistiques()
print() 
bibliotheque.emprunter_livre("harry potter", "Alice Dupont")
bibliotheque.emprunter_livre("le seigneur des anneaux", "Bob Martin")
bibliotheque.emprunter_livre("le petit prince", "Charlie Brown")    
bibliotheque.statistiques()
print()
bibliotheque.rendre_livre("harry potter")
