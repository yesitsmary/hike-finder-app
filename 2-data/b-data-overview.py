# Preview of data
print(f"Fetched {len(df)} Hiking Activities")
df.head(10)
df.info()
df.isnull().sum()

# Note: 'states' and 'season' have multiple values

# List of national parks
print("
List of National Parks:")
national_parks = df[df['parkName'].str.contains("National Park", na=False)] # Filter only names containing "National Park"
park_counts = national_parks['parkName'].value_counts() # Count the occurrences
pd.set_option('display.max_rows', None) # Show all rows in pandas output
print(park_counts)


# Trail duration counts
print("
Trail Duration Count:")
pd.set_option('display.max_rows', None) # Show all rows in pandas output
print(df['duration'].value_counts())