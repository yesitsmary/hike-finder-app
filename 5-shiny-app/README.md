## 📁 File Overview

- `shiny_app.py`: Main PyShiny app file with dropdowns for energy level and park location. Sends user input to the Flask API for trail recommendations.

## 🌐 Shiny Testing & Deploy Instructions

This section explains how to test and deploy the Hike Finder app using Shiny.

### 1. Install the necessary packages

```bash
pip3 install shiny
pip3 install requests
```
### 2. Run the app locally

```bash
shiny run --reload shiny_app.py
```
*This will launch a local server at http://localhost:8000. Open it in your browser to interact with the app.*

### 2. Deploy to shinyaps.io

```bash
rsconnect deploy shiny ~/Desktop \
  --name yesitsmary \
  --title hike-finder-app
```
*Make sure you’ve installed rsconnect-python and authenticated with rsconnect login*
