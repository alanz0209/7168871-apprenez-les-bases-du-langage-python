def salaire_mensuelle(salaire_annuel):
    salaire_mensuelle = salaire_annuel / 12
    return salaire_mensuelle

def salaire_hebdomadaire(salaire_mensuel):
    salaire_hebdomadaire = salaire_mensuel / 4
    return salaire_hebdomadaire

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    salaire_horaire = salaire_hebdomadaire / heures_travaillees
    return salaire_horaire

salaire_annuel = float(input("Entrez votre salaire annuel : "))
heures_travaillees = float(input("Entrez le nombre d'heures travaillées par semaine : "))
mensuel = salaire_mensuelle(salaire_annuel)
hebdomadaire = salaire_hebdomadaire(mensuel)
horaire = salaire_horaire(salaire_hebdomadaire, heures_travaillees)


print("Votre salaire horaire est : ", horaire, "euros")

