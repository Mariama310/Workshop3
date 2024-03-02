
from flask import Flask, request, jsonify
from sklearn.externals import joblib
# Charger le modèle SVM préalablement sauvegardé
svm_model = joblib.load('svm_model.pkl')

app = Flask(__name__)

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

