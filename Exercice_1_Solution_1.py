
def transform(chain):
    # Conversion des chaînes en listes d'entiers
    list1 = [int(i) for i in chain[0].split(',')]
    list2 = [int(i) for i in chain[1].split(',')]

    # Trouver l'intersection des deux listes
    intersection = [value for value in list1 if value in list2]

    # Trier les entiers de l'intersection
    intersection.sort()

    # Créer une chaîne de caractères avec les entiers triés et la concaténation du nom, prénom et classe
    nom_prenom_classe = "MAGNIKOUWE_Fabrice_MasterIA"
    result = ', '.join(map(str, intersection)) + ": " + nom_prenom_classe

    return result

# Exécution de la fonction
if __name__ == "__main__":
    arr1 = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
    out = transform(arr1)
    print(out)  # doit afficher ---> 31, 4, 1:nom_prenom_classe

    arr3 = ["9, 3, 5, 7, 14", "10, 2, 6, 16, 15"]
    out = transform(arr3)
    print(out)  # doit afficher ---> 15, 7, 5:nom_prenom_classe
