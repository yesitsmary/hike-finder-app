# Hike Finder API

This project is a Flask-based machine learning API that predicts the energy level (mood) of a hiking trail based on its description. It uses a logistic regression model trained on TF-IDF features and an elevation gain indicator.

## 🚀 Features

- Text classification using TF-IDF + Logistic Regression
- Binary flag for elevation gain using regex
- Flask API to predict energy level: Relaxed, Chill, Adventurous, or Challenging
- Dockerized for easy deployment
- Tested locally with `curl` and ready for deployment

## 🧠 Model Overview

- **Text input:** Trail descriptions from the National Park Service API
- **Preprocessing:** Strip HTML, detect elevation gain
- **Features:** TF-IDF (1000 unigrams) + `hasElevation` binary flag
- **Model:** Multiclass Logistic Regression
- **Classes:** `Relaxed`, `Chill`, `Adventurous`, `Challenging`

## 📁 File Overview

- app.py: Flask app to serve model
- model.pkl: Trained logistic regression model
- vectorizer.pkl: Fitted TF-IDF vectorizer
- requirements.txt: Python dependencies
- Dockerfile: Docker build instructions
- README.md: Project overview

## 🐳 Docker Build Instructions

This section explains how to build and run the Flask-based Hiking Finder API using Docker and optionally push it to Docker Hub.

### 1. Clone repo and change directory

```bash
git clone https://github.com/your-username/hike-finder-api.git
cd hike-finder-api
```

### 2. Build and run Docker container
```bash
docker build -t hike-finder-api .
docker run -p 8080:8080 hike-finder-api
```

### 3. Tag and push to Docker Hub
#### *This step is only required if you plan to deploy to a cloud platform like Google Cloud Run.*
```bash
docker tag hike-finder-api maryv8/hike-finder-api:latest
docker push maryv8/hike-finder-api:latest
```

### 4. Send a test prediction
```bash
curl -X POST http://127.0.0.1:8080/predict \
     -H "Content-Type: application/json" \
     -d '{"longDescription": "This trail includes an elevation gain of 1,500 feet over rocky terrain."}'
```
