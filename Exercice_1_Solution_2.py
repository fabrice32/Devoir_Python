def transform(chain):
    # Conversion des chaînes en listes d'entiers, puis en ensembles
    set1 = set(int(i) for i in chain[0].split(','))
    set2 = set(int(i) for i in chain[1].split(','))

    # Trouver l'intersection des deux ensembles
    intersection = set1 & set2

    # Convertir l'intersection en liste et la trier
    intersection = sorted(list(intersection))

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