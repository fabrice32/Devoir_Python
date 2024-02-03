import sqlite3

def trouver_nombre_manquant(nombre_tableau):
    # Trier le tableau
    nombre_tableau.sort()

    # Trouver les nombres manquants
    nombres_manquants = []
    for i in range(1, len(nombre_tableau)):
        if nombre_tableau[i] - nombre_tableau[i-1] > 1:
            nombres_manquants.append(nombre_tableau[i-1] + 1)

    # Se connecter à la base de données SQLite
    conn = sqlite3.connect('nombre_manquant.db')

    # Créer une table pour stocker les nombres manquants
    conn.execute('CREATE TABLE IF NOT EXISTS nombre_manquant (nombre INTEGER PRIMARY KEY)')

    # Insérer les nombres manquants dans la table
    for nombre_manquant in nombres_manquants:
        conn.execute('INSERT OR IGNORE INTO nombre_manquant (nombre) VALUES (?)', (nombre_manquant,))

    # Valider la transaction
    conn.commit()

    # Fermer la connexion
    conn.close()

    return nombres_manquants

# Exemple
nombre_tableau = [4, 6, 8, 9, 10]
nombres_manquants = trouver_nombre_manquant(nombre_tableau)
print(f'Les nombres manquants sont {nombres_manquants}')