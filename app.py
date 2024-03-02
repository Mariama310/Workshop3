from flask import Flask, request, jsonify
from sklearn.externals import joblib

app = Flask(__name__)

# Charger le modèle SVM préalablement sauvegardé
svm_model = joblib.load('svm_model.pkl')

@app.route('/svm/predict', methods=['POST'])
def predict_svm():
    # Récupérer les données d'entrée depuis la requête POST
    data = request.json
    
    # Utiliser le modèle SVM pour faire une prédiction
    prediction = svm_model.predict([data['features']])[0]
    
    # Renvoyer la prédiction au format JSON
    return jsonify({'prediction': prediction}), 200

# Charger le modèle d'Arbres de Décision préalablement sauvegardé
decision_tree_model = joblib.load('dt_model.pkl')

@app.route('/decision-tree/predict', methods=['POST'])
def predict_decision_tree():
    # Récupérer les données d'entrée depuis la requête POST
    data = request.json
    
    # Utiliser le modèle d'Arbres de Décision pour faire une prédiction
    prediction = decision_tree_model.predict([data['features']])[0]
    
    # Renvoyer la prédiction au format JSON
    return jsonify({'prediction': prediction}), 200

if __name__ == '__main__':
    app.run(debug=True)


# Génération de la prédiction de consensus
@app.route('/consensus/predict', methods=['POST'])
def predict_consensus():
    # Récupérer les données d'entrée depuis la requête POST
    data = request.json
    
    # Envoyer des requêtes aux API des modèles individuels (SVM et Arbre de Décision)
    svm_response = requests.post('http://127.0.0.1:5000/svm/predict', json=data)
    dt_response = requests.post('http://127.0.0.1:5000/decision-tree/predict', json=data)
    
    # Extraire les prédictions de chaque modèle
    svm_prediction = svm_response.json()['prediction']
    dt_prediction = dt_response.json()['prediction']
    
    # Calculer la prédiction de consensus (moyenne des prédictions)
    consensus_prediction = (svm_prediction + dt_prediction) / 2
    
    # Renvoyer la prédiction de consensus au format JSON
    return jsonify({'consensus_prediction': consensus_prediction}), 200
