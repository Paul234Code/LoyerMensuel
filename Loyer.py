#!/usr/bin/bash
TotalLoyerMensuel = input("Donner le montant Total du loyer:")
LoyerMensuel = int(TotalLoyerMensuel)
print("Total du Loyer Mensuel :", LoyerMensuel)


# Calcul du loyer individuel par /mois
def calculLoyer():
    return LoyerMensuel / 3


InternetMensuel = float(input(" Donner le montant de la facture internet svp:"))
print("TotalInternet_mensuel = :", InternetMensuel)


# calcul du montant d'internet par personne
def calculInternet():
    return InternetMensuel / 3


Divers_Paul = float(input("Donner le montant Divers payer par Paul:"))
Divers_Sidy = float(input("Donner le montant Divers payer par Sidy:"))
Divers_Accrachi = float(input("Donner le montant Divers payer par Accrachi:"))
# affichage des montants de chaque divers
print("Divers_Paul: {:6.2f}".format(Divers_Paul))
print("Divers_Sidy: {:6.2f}".format(Divers_Sidy))
print("Divers_Accrachi: {:6.2f}".format(Divers_Accrachi))


# calcul du total des Divers
def calculPaulDivers():
    return (Divers_Paul / 3) + (Divers_Sidy / 3) + (Divers_Accrachi / 3)


def calculSidyDivers():
    return (Divers_Paul / 3) + (Divers_Sidy / 3) + (Divers_Accrachi / 3)


def calculAccrachiDivers():
    return (Divers_Paul + Divers_Sidy + Divers_Accrachi) / 3


# calcul du montant du dans les Divers par locataire


print("Partie Loyer Mensuel:")

# calcul internet par mois/par personne
print()
print("Loyer_Paul: {:6.2f}".format(calculLoyer()))
print("Loyer_Sidy: {:6.2f}".format(calculLoyer()))
print("Loyer_Accrachi: {:6.2f}".format(calculLoyer()))
# calcul de la facture internet
print("Internet Mensuel :\n")

print("Internet_Paul:      {:6.2f}".format(calculInternet()))
print("Internet_Sidy:      {:6.2f}".format(calculInternet()))
print("Internet_Accrachi:    {:6.2f}".format(calculInternet()))

print("Partie des Divers :\n")

print("Divers_Paul:      {:6.2f}".format(calculPaulDivers()))
print("Divers_Sidy:      {:6.2f}".format(calculSidyDivers()))
print("Divers_Accrachi:      {:6.2f}".format(calculAccrachiDivers()))
# total pour chaque personne
Total_Paul = calculLoyer() + calculInternet() + calculPaulDivers() - Divers_Paul
Total_Sidy = calculLoyer() + calculInternet() + calculSidyDivers() - Divers_Sidy
Total_Accrachi = calculLoyer() + calculInternet() + calculAccrachiDivers() - Divers_Accrachi - InternetMensuel
print("Total pour chaque personne:\n")
print("Total de Paul:  {:6.2f}$".format(Total_Paul))
print("Total de Sidy:  {:6.2f}$".format(Total_Sidy))
print("Total d'Accrachi : {:6.2f}$".format(Total_Accrachi))
print("Total des frais mensuel: {:6.2f}$".format(Total_Sidy + Total_Paul + Total_Accrachi))
