# 🏞️ Hike Finder App

A machine learning project that recommends hiking trails in U.S. National Parks based on your **mood** (energy level). It combines a Flask API for predictions with a PyShiny app for a clean user interface.

👉 **Check it out:** [yesitsmary.shinyapps.io/hike-finder-app](https://yesitsmary.shinyapps.io/hike-finder-app/)

## 🧪 Features

- Logistic regression trained on TF-IDF + elevation cues
- Binary flag for elevation gain using regex
- Flask API for text-based predictions
- Dockerized backend for easy deployment
- Shiny app frontend with dropdowns for energy level and park

## 📁 Folder Structure
- **1-presentations:** Class presentations
- **2-data:** Collection, cleaning, & EDA scripts
- **3-model:** Trained model + vectorizer
- **4-flask-api:** Flask backend with model & prediction endpoint
- **5-shiny-app:** PyShiny frontend interface
- **README.md:** You're here!
