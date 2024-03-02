from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Fonction pour établir une connexion à la base de données
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Route pour récupérer tous les produits
@app.route('/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    conn.close()
    return jsonify([dict(row) for row in products])

# Route pour récupérer un produit par son ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
    product = cursor.fetchone()
    conn.close()
    if product:
        return jsonify(dict(product)), 200
    else:
        return jsonify({'error': 'Product not found'}), 404

# Route pour ajouter un nouveau produit
@app.route('/products', methods=['POST'])
def add_product():
    new_product = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Products (name, description, price, category, stock) VALUES (?, ?, ?, ?, ?)',
                   (new_product['name'], new_product['description'], new_product['price'],
                    new_product['category'], new_product['stock']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Product added successfully'}), 201

# Route pour mettre à jour un produit par son ID
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    updated_product = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE Products SET name = ?, description = ?, price = ?, category = ?, stock = ? WHERE id = ?',
                   (updated_product['name'], updated_product['description'], updated_product['price'],
                    updated_product['category'], updated_product['stock'], product_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Product updated successfully'}), 200

# Route pour supprimer un produit par son ID
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Products WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Product deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
