from temperature import Temperature

def test_temperature():
    print("=== TESTS DE LA CLASSE TEMPERATURE ===\n")

    print("→ Création d'une température à 22.5°C")
    t1 = Temperature(22.5)
    print(f"  Celsius : {t1.valeur_celsius}°C")
    print(f"  Fahrenheit : {t1.fahrenheit}°F")
    print(f"  Kelvin : {t1.kelvin}K")
    print(f"  État : {t1.etat}\n") 

    print("→ Création depuis 32°F (0°C)")
    t2 = Temperature.depuis_fahrenheit(32)
    print(f"  Celsius : {t2.valeur_celsius}°C")
    print(f"  État : {t2.etat}\n")

    print("→ Comparaison : t1 (liquide) vs t2 (solide)")
    print(f"  t1.etat = {t1.etat}, t2.etat = {t2.etat}")
    print(f"  Compatible ? {t1.est_compatible_avec(t2)}\n")

    t3 = Temperature(50)
    print("→ Comparaison : t1 (liquide) vs t3 (liquide)")
    print(f"  Compatible ? {t1.est_compatible_avec(t3)}\n")

    print("→ Tentative de création à -300°C (zéro absolu)")
    try:
        Temperature(-300)
    except ValueError as e:
        print(f" Erreur capturée : {e}")
    print()

    print("→ Tentative de création avec True")
    try:
        Temperature(True)
    except TypeError as e:
        print(f" Erreur capturée : {e}")
    print()

    print("→ Tentative de création avec chaîne")
    try:
        Temperature("25")
    except TypeError as e:
        print(f" Erreur capturée : {e}")
    print()

    print("→ Tentative de comparaison avec un objet non Temperature")
    try:
        t1.est_compatible_avec("25°C")
    except TypeError as e:
        print(f" Erreur capturée : {e}")
    print()

    try:
        Temperature(1_000_001)
    except ValueError as e:
        print(f" Erreur capturée : {e}")
    print()

    print("🫡 Tous les tests ont réussi !")

if __name__ == "__main__":
    test_temperature()