import sqlite3

# Connexion à la base de données (crée un fichier database.db s'il n'existe pas)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Création de la table Products
cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT,
                    price REAL NOT NULL,
                    category TEXT,
                    stock INTEGER NOT NULL
                )''')

# Enregistrer les modifications et fermer la connexion
conn.commit()
conn.close()
