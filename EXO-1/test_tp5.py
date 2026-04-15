from produit import Produit
from produit_electronique import ProduitElectronique
from produit_alimentaire import ProduitAlimentaire

print("=== TEST TP5 — Hiérarchie de produits ===\n")

clavier = ProduitElectronique("KB-001", "Clavier RGB", 79.99, 15, 24, 0.5)
fromage = ProduitAlimentaire("ALI-001", "Comté", 12.99, 50, "2025-06-15")

print("1. Frais de livraison (polymorphisme) :")
print(f"   Clavier : {clavier.calculer_frais_livraison()}€")  
print(f"   Fromage : {fromage.calculer_frais_livraison()}€")  

print("\n2. Affichage détails :")
print("   Clavier :")
clavier.afficher_details()
print("   Fromage :")
fromage.afficher_details()

print("\n3. Péremption :")
print(f"   Fromage périmé ? {fromage.est_perime()}")  

print("\n4. Propriété héritée (prix_ttc) :")
print(f"   Clavier TTC : {clavier.prix_ttc}€")  
print(f"   Fromage TTC : {fromage.prix_ttc}€")  

print("\n5. Vérification que Produit ne peut pas être instancié :")
try:
    p = Produit("X", "X", 10, 5)
    print("   ✗ ERREUR : Produit a été créé directement !")
except TypeError as e:
    print(f"   ✓ TypeError levée : {e}")