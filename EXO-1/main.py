from voiture import Voiture

voiture1 = Voiture("Renault", "Clio", 2018, 50000, 15000)
voiture2 = Voiture("Peugeot", "208", 2021, 20000, 18000)
voiture3 = Voiture("Citroën", "C3", 2019, 80000, 14000)

print(f"Nombre total de voitures créées: {Voiture.nb_voitures}")
print()

print("Informations des voitures:")
voiture1.afficher()
print()
voiture2.afficher()
print()
voiture3.afficher()
print()

print("Voitures récentes (>= 2020):")
print(f"Voiture 1 (Renault Clio {voiture1.annee}): {voiture1.est_recente()}")
print(f"Voiture 2 (Peugeot 208 {voiture2.annee}): {voiture2.est_recente()}")
print(f"Voiture 3 (Citroën C3 {voiture3.annee}): {voiture3.est_recente()}")
print()

print("Simulation de parcours:")
voiture1.parcourir(1000)
voiture2.parcourir(500)
print(f"Voiture 1 après 1000 km: {voiture1.kilometrage} km")
print(f"Voiture 2 après 500 km: {voiture2.kilometrage} km")
print()

# Estimation de la valeur
print("Estimation de la valeur actuelle:")
print(f"Voiture 1: {voiture1.estimer_valeur()} €")
print(f"Voiture 2: {voiture2.estimer_valeur()} €")
print(f"Voiture 3: {voiture3.estimer_valeur()} €")