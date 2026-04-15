from compte_securise import CompteBancaire

def main():
    print("=== DÉMONSTRATION DU COMPTE BANCAIRE SÉCURISÉ ===\n")

    c = CompteBancaire("Bob", 1000, 500)
    print(f"Compte de {c.titulaire} : solde = {c.solde}€, découvert = {c.decouvert_autorise}€")

    print("\n→ Dépôt de 200€")
    c.deposer(200)

    print("\n→ Retrait de 1500€")
    c.retirer(1500)

    print("\n→ Retrait de 100€")
    c.retirer(100)

    print("\n→ Historique des opérations")
    c.afficher_historique()

    print(f"\n→ Est à découvert ? {c.est_a_decouvert}")
    print(f"→ Nombre d'opérations : {c.nb_operations}")

    print("\n→ Appliquer les intérêts...")
    c.appliquer_interets()
    print(f"Solde après intérêts : {c.solde}")

    print("\n→ Tentative de modification du titulaire")
    try:
        c.titulaire = "  "
    except ValueError as e:
        print(f" Erreur : {e}")

    print("\n Fin de la démonstration.")

if __name__ == "__main__":
    main()
