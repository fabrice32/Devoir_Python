import operator

# Création de la première liste en utilisant une boucle for
first_list = []
for i in range(1200, 2000, 135):
    first_list.append(i)

# Création de la deuxième liste en utilisant une boucle for
first_list_even = []
for i in first_list:
    if i % 2 == 0:
        first_list_even.append(i)

# Ajout des nombres pairs dans la liste numbers
numbers = first_list_even[:]

# Création de la liste des nombres pairs multipliés par 2
multiplied_by_two = []
for i in numbers:
    multiplied_by_two.append(i * 2)

# Création de la liste des nombres pairs multipliés par 2 (filtrage)
o = []
for i in multiplied_by_two:
    if i % 2 == 0:
        o.append(i)

# Création de la liste des nombres impairs (filtrage)
e = []
for i in numbers:
    if i % 2 != 0:
        e.append(i)

# Affichage des résultats
print(first_list)
print(numbers)
print(o)
print(e)