import sqlite3
import numpy as np

def find_missing_number(numbers):
    # Calcul de la somme attendue
    expected_sum = np.arange(min(numbers), max(numbers) + 1).sum()

    # Calcul de la somme
    actual_sum = np.sum(numbers)

    # Trouver le nombre manquant
    missing_number = np.setdiff1d(np.arange(min(numbers), max(numbers) + 1), numbers).item()

    # Connection à SQLite
    conn = sqlite3.connect('missing_numbers.db')

    # Creation de la table
    conn.execute('CREATE TABLE IF NOT EXISTS missing_numbers (number INTEGER)')

    # Insertion dans la table
    conn.execute('INSERT INTO missing_numbers (number) VALUES (?)', (missing_number,))

    # Commit the transaction
    conn.commit()

    # Close the connection
    conn.close()

    return missing_number

# Exemple
numbers = [1, 2, 3, 5, 6, 7, 8]
missing_number = find_missing_number(numbers)
print(f'The missing number is {missing_number}')