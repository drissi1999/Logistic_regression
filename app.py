from flask import Flask, request, jsonify
import numpy as np
import joblib

# Load the model and scaler
model = joblib.load('best_nba_classifier.pkl')
scaler = joblib.load('scaler.pkl')

# Define feature columns
feature_cols = ['GP', 'MIN', 'PTS', 'FGM', 'FGA', 'FG%', '3P Made', '3PA', 
                '3P%', 'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 
                'STL', 'BLK', 'TOV']

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>NBA Player Classification API</h1>"

@app.route('/api/predict', methods=['POST'])
def api_predict():
    data = request.get_json(force=True)
    
    # Extract features from request data
    try:
        features = [data[feature] for feature in feature_cols]
    except KeyError as e:
        return jsonify({'error': f'Missing feature: {e}'}), 400
    
    features = np.array(features).reshape(1, -1)
    features_scaled = scaler.transform(features)
    
    # Make prediction
    prediction = model.predict(features_scaled)
    output = int(prediction[0])
    
    result = 'VOUS POUVEZ RECRUTER!' if output == 1 else 'NE RECRUTEZ PAS!'
    return jsonify({'recruit': output, 'decision': result})


if __name__ == '__main__':
    app.run(debug=True, port=8080)