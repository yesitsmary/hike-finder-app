## 🧠 Model Overview

- **Text input:** Trail descriptions from the National Park Service API
- **Preprocessing:** Strip HTML, detect elevation gain
- **Features:** TF-IDF (1000 unigrams) + `hasElevation` binary flag
- **Model:** Multiclass logistic regression
- **Classes:** `Relaxed`, `Chill`, `Adventurous`, `Challenging`

## 📁 File Overview

- model.pkl: Trained logistic regression model
- vectorizer.pkl: Fitted TF-IDF vectorizer
- hiking_trails.csv: Cleaned data
