## 📁 File Overview

- `a-data-collection.py`  
  Collects ~1,500 activities from the National Park Service API, filters for hiking-specific trails   
   and stores results in a structured pandas DataFrame.

- `b-data-overview.py`  
  Provides exploratory insights into the dataset, including trail counts, missing values, and a    
  breakdown of trail durations and national park frequency.

- `c-data-cleaning.py`  
  Converts duration strings (e.g., half day, 1–2 hours) into numeric minutes using regular expressions    
  for standardization.

- `d-data-analysis.py`  
  Categorizes trails into energy levels (`Relaxed`, `Chill`, `Adventurous`, `Challenging`) based on    
  duration and generates a bar chart showing trail count by mood (see below).

![energy-bar-chart](https://github.com/user-attachments/assets/00535f59-3aa4-4720-9383-03bc4f84ecaf)
