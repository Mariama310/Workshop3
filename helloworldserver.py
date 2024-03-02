from flask import Flask, request, jsonify

app = Flask(__name__)

# Définir l'URL du serveur "Hello World"
server_url = 'http://localhost:5000'

# Route pour le serveur "Hello World"
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Route pour le registre DNS
@app.route('/getServer')
def get_server():
    return jsonify({'code': 200, 'server': server_url})

if __name__ == '__main__':
    app.run(debug=True)
