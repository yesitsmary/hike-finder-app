## 📁 File Overview

- `app.py`: Flask app to serve model
- `requirements.txt`: Python dependencies
- `Dockerfile`: Docker build instructions

## 🐳 Docker Build Instructions

This section explains how to build and run the Flask-based Hiking Finder API using Docker and optionally push it to Docker Hub.

### 1. Clone repo and change directory

```bash
git clone https://github.com/yourusername/hike-finder-api.git
cd hike-finder-api
```
*Downloads project folder from Github and moves you into the folder.*

### 2. Build and run Docker container
```bash
docker build -t hike-finder-api .
```
*Builds the Docker image from the Dockerfile and tags it as hike-finder-api.*
```bash
docker run -p 8080:8080 hike-finder-api
```
*Runs the app in a Docker container and makes it accessible at http://localhost:8080.*

### 3. Tag and push to Docker Hub (Optional)
```bash
docker tag hike-finder-api yourusername/hike-finder-api:latest
```
*Adds a tag that points to the Docker Hub repository.*

```bash
docker push yourusername/hike-finder-api:latest
```
*Pushes the image to Docker Hub for deployment.*

### 4. Send a test prediction
```bash
curl -X POST http://127.0.0.1:8080/predict \
     -H "Content-Type: application/json" \
     -d '{"longDescription": "Looking for a chill hike in Zion", "parkName": "Zion National Park"}'
```
*Ensures the API works correctly.*
