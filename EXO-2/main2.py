from compte import CompteBancaire

compte1 = CompteBancaire("Alice Dupont", 1000.0, 200.0)
compte2 = CompteBancaire("Bob Martin", 500.0)

compte1.deposer(200.0)
print(f"Solde d'Alice après dépôt : {compte1.solde}€")

compte1.retirer(150.0)
print(f"Solde d'Alice après retrait : {compte1.solde}€")

compte1.retirer(1200.0)  

compte1.virement(compte2, 300.0)
print(f"Solde d'Alice après virement : {compte1.solde}€")
print(f"Solde de Bob après virement : {compte2.solde}€")

compte1.appliquer_interets()
compte2.appliquer_interets()

compte1.afficher_historique()
print()
compte2.afficher_historique()