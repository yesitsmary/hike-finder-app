## 📁 File Overview

- model.pkl: Trained logistic regression model
- vectorizer.pkl: Fitted TF-IDF vectorizer
- hiking_trails.csv: Cleaned and preprocessed dataset

## 🧠 Model Overview

- **Text Input:** Long descriptions of hiking trails from the NPS API
- **Preprocessing:** 
  - Strip HTML tags (e.g., `<li>`, `<br>`)
  - Binary flag for elevation gain using regex (`hasElevation`)
- **Features:** 
  - TF-IDF vectors (top 1000 unigrams, stop words removed)
  - Binary elevation feature combined using `scipy.sparse.hstack`
- **Model:** Multiclass logistic regression (4-way classification)
- **Target Classes:** `Relaxed`, `Chill`, `Adventurous`, `Challenging`
- **Training Details:** 80/20 train-test split with stratified sampling
