import requests
import pandas as pd
from google.colab import files
from IPython.display import display

API_KEY = "EblhkgZEt0DqqJCrLNae8G1YNffURTI7Tnkhscoh"

headers = {
    "X-Api-Key": API_KEY
}

# Prepare to iterate over pages of API results (100 at a time from 0 to 1,499)
flat_items = []

for start in range(0, 1500, 100):

    # Define query parameters to fetch up to 100 activities at a time that match "hike"
    params = {
        "limit": 100,
        "start": start,
        "q": "hiking"
    }

    # Send GET request to NPS “Things to Do” endpoint and parse response as JSON
    response = requests.get("https://developer.nps.gov/api/v1/thingstodo", headers=headers, params=params)
    data = response.json()

    # Loop over activity items and filter only those with "Hiking" listed in the activities
    for item in data.get("data", []):
        if any(act.get("name", "").lower() == "hiking" for act in item.get("activities", [])):

            # Extract name and state of the first related park (if available)
            related_parks = item.get("relatedParks", [])
            park_name = related_parks[0].get("fullName", "") if related_parks else ""
            states = related_parks[0].get("states", "") if related_parks else ""

            # Add cleaned-up, flattened dictionary to flat_items list
            flat_items.append({
                "title": item.get("title", ""),
                "duration": item.get("duration", ""),
                "season": ", ".join(item.get("season", [])),
                "parkName": park_name,
                "states": states,
                "url": item.get("url", ""),
                "shortDescription": item.get("shortDescription", ""),
                "longDescription": item.get("longDescription", ""),
                "activity": "Hiking"
            })

# Convert list of dictionaries into a pandas DataFrame
df = pd.DataFrame(flat_items)

# Look at one full activity dictionary from the API (if needed)
# import json
# print(json.dumps(data["data"][0], indent=2))

# Show full dataframe with scrollable columns (if needed)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_colwidth', None)
# display(df.head(10))