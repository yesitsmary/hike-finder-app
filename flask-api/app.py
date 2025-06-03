
import os
import re # For working with regular expressions
import joblib # For loading the saved model and vectorizer
import numpy as np # For numeric operations (used here to build input arrays)
import pandas as pd
from scipy.sparse import hstack # To horizontally stack sparse matrices
from flask import Flask, request, jsonify # For building the web API

# Load model and vectorizer once globally
clf = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Load hiking trails CSV once globally
df = pd.read_csv("hiking_trails.csv")

# Create Flask app instance
app = Flask(__name__)

# Function to strip HTML tags
def strip_html_tags(text):
    return re.sub(r"<[^>]+>", "", text)

# Function to detect elevation gain
def has_elevation_gain(desc):

    pattern = r"(ascend|ascent|climb|elevation|gain|incline)(?:\W+\w+){0,8}?\W+(\d{2,5})"
    return int(bool(re.search(pattern, desc.lower()))) # Returns 1 if pattern matches, 0 otherwise

# Set up API to predict route
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json  # Parse incoming JSON data from POST request

    raw_desc = data.get("longDescription", "") # Extract the description field, fallback to empty string
    park_name = data.get("parkName", "") # Extract the park name, fallback to empty string

    clean_desc = strip_html_tags(raw_desc) # Remove HTML
    elevation_flag = has_elevation_gain(clean_desc) # Check if description mentions elevation gain
    
    # Vectorize and predict energy level
    X_text = vectorizer.transform([clean_desc]) # Convert cleaned description to TF-IDF feature vector
    X = hstack([X_text, np.array([[elevation_flag]])]) # Combine text and elevation feature
    prediction = clf.predict(X)[0] # Use the model to predict the energy level (returns one label)

    # For debugging (if needed)
    print("------ NEW REQUEST ------")
    print("Received data:", data)
    print("Cleaned description:", clean_desc)
    print("Predicted energy level:", prediction)
    print("Park name:", park_name)

    # Filter for matching prediction and park name
    matching = df[
        (df["predicted_energy_level"] == prediction) &
        (df["parkName"].str.lower().str.contains(park_name.lower().strip(), na=False))
    ]

    print("Matching rows:", matching.shape[0])

    if not matching.empty:
        trail = matching.iloc[0]
        print("Returning trail:", trail["title"])
        return jsonify({
            "title": trail["title"],
            "shortDescription": trail["shortDescription"],
            "duration": trail["duration"],
            "url": trail["url"]
        })
    else:
        return jsonify({
            "title": "No Trail Found",
            "shortDescription": "Try a different park or energy level.",
            "duration": "-",
            "url": ""
        })

# Run Flask app locally
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=False, host="0.0.0.0", port=port)
