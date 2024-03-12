# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 08:09:49 2024

@author: anjan
"""

import joblib
import sklearn
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
import pandas as pd

def score(text: str, threshold: float) -> tuple[bool, float]:
    """
    Scores a trained model on a given text.

    Args:
        text (str): The input text to be scored.
        model (sklearn.estimator): The trained model for scoring.
        threshold (float): The decision threshold for classification.

    Returns:
        tuple[bool, float]: A tuple containing the prediction (True for spam, False for non-spam)
            and the propensity score (between 0 and 1).
    """
    # Load the trained model from a file 
    model = joblib.load('best_model.pkl')['clf']
    train = pd.read_csv( 'train.csv') 
    X,y = train['text'], train['label']
    
    
    vectorizer = TfidfVectorizer(stop_words='english')
    vectorizer.fit(X)
    
    
    text = vectorizer.transform([text])
    
    
    # Make predictions using the loaded model
    propensity = model.predict_proba(text)[0][1]  # Probability of being spam
    prediction = bool(propensity >= threshold)
    
    return prediction, propensity

