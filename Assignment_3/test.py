# test.py
import os
import joblib
import requests
import subprocess
import time
import pytest
from score import score
from app import app

def test_score():
    # Test the score function with different scenarios
    text = "Test text"
    threshold = 0.5
    
    # Smoke test
    prediction, propensity_score = score(text, threshold)
    assert prediction is not None
    assert propensity_score is not None

    # Format test
    assert isinstance(prediction, bool)
    assert isinstance(propensity_score, float)

    # Prediction value test
    assert prediction in [False, True]

    # Propensity score range test
    assert 0 <= propensity_score <= 1

    # Threshold tests
    assert score(text, threshold=0)[0]  # If threshold is 0, prediction should always be True
    assert not score(text, threshold=1)[0]  # If threshold is 1, prediction should always be False

    # Obvious spam input text test
    spam_text = "Congratulations! You've won a free trip to Hawaii..."
    assert score(spam_text, threshold=0.5)[0]

    # Obvious non-spam input text test
    non_spam_text = "Hello, how are you?"
    assert not score(non_spam_text, threshold=0.5)[0]

    print('All test cases for score function passed successfully.')

@pytest.fixture
def app_url():
    return 'http://127.0.0.1:5000'

def test_score_endpoint(app_url):
    # Test the Flask endpoint
    payload = {'text': 'Test text'}
    response = requests.post(f'{app_url}/score', json=payload)
    assert response.status_code == 200
    data = response.json()
    assert 'prediction' in data
    assert 'propensity' in data
    assert isinstance(data['prediction'], bool)
    assert isinstance(data['propensity'], float)

    print('Flask endpoint test passed successfully.')

def test_flask():
    # Test the Flask app
    text = "Test text"
    threshold = 0.5

    flask_process = subprocess.Popen(["python", "app.py"], stdout=subprocess.PIPE, shell=True)
    time.sleep(2)

    payload = {'text': text}
    response = requests.post('http://127.0.0.1:5000/score', json=payload)
    data = response.json()
    
    prediction = data['prediction']
    propensity = data['propensity']

    assert response.status_code == 200
    assert 'prediction' in data
    assert 'propensity' in data
    assert prediction in [False, True]
    assert 0 <= propensity <= 1

    flask_process.terminate()

    print('Flask app test passed successfully.')

if __name__ == "__main__":
    pytest.main([__file__])
