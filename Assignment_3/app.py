# app.py
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the best model saved during experiments
best_model = joblib.load("best_model.pkl")

@app.route('/score', methods=['POST'])
def score():
    data = request.json
    text = data['text']
    threshold = 0.5  # You might want to make this configurable
    prediction, propensity_score = score_text(text, threshold)
    return jsonify({'prediction': prediction, 'propensity': propensity_score})

def score_text(text, threshold):
    # Your scoring logic here, using the loaded model
    # This is just a placeholder, replace it with your actual scoring logic
    return True, 0.7

if __name__ == '__main__':
    app.run(debug=True)

