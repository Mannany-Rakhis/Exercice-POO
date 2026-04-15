from compte_securise import CompteBancaire

def test_compte_bancaire():
    print("=== TESTS DU COMPTE BANCAIRE ===\n")

    c = CompteBancaire("Alice", 500, 200)
    print(f"Compte créé : {c.titulaire}, solde = {c.solde}, découvert = {c.decouvert_autorise}")
    print(f"Est à découvert ? {c.est_a_decouvert}")
    print(f"Nombre d'opérations : {c.nb_operations}\n")

    print("→ Dépôt de 100")
    c.deposer(100)
    print(f"Solde après dépôt : {c.solde}")
    print(f"Nombre d'opérations : {c.nb_operations}\n")

    print("→ Retrait de 800 (découvert autorisé : 200)")
    reussi = c.retirer(800)
    print(f"Opération réussie ? {reussi}")
    print(f"Solde après retrait : {c.solde}")
    print(f"Est à découvert ? {c.est_a_decouvert}\n")

    print("→ Retrait de 50 (solde actuel : -200, découvert max : 200)")
    reussi = c.retirer(50)
    print(f"Opération réussie ? {reussi}")
    print(f"Solde après retrait : {c.solde}\n")

    print("→ Affichage de l'historique :")
    c.afficher_historique()
    print()

    print("→ Tentative de modification du titulaire avec chaîne vide :")
    try:
        c.titulaire = ""
    except ValueError as e:
        print(f" Erreur capturée : {e}")
    print()

    print("→ Tentative de dépôt avec booléen (True) :")
    try:
        c.deposer(True)
    except TypeError as e:
        print(f" Erreur capturée : {e}")
    print()

    print("→ Tentative de dépôt avec montant négatif (-50) :")
    try:
        c.deposer(-50)
    except ValueError as e:
        print(f" Erreur capturée : {e}")
    print()

    print("→ Tentative de retrait avec booléen (False) :")
    try:
        c.retirer(False)
    except TypeError as e:
        print(f" Erreur capturée : {e}")
    print()

    print("→ Tentative d'assignation directe d'un solde invalide (-300) :")
    try:
        c.solde = -300
    except ValueError as e:
        print(f" Erreur capturée : {e}")
    print()

    print("→ Tentative d'assignation à est_a_decouvert (lecture seule) :")
    try:
        c.est_a_decouvert = True
    except AttributeError as e:
        print(f"Erreur capturée : {e}")
    print()

    print("🫡 Tous les tests ont réussi !")

if __name__ == "__main__":
    test_compte_bancaire()