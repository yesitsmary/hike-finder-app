# Create energy tags
def energy_level(minutes):
    if minutes is None:
        return "Unknown"
    elif minutes <= 45: # 45 minutes or less
        return "Relaxed"
    elif minutes <= 120: # up to 2 hours
        return "Chill"
    elif minutes <= 300: # up to 5 hours
        return "Adventurous"
    else:
        return "Challenging" # over 5 hours

df["durationMinutes"] = df["duration"].apply(duration_to_minutes)
df["energyLevel"] = df["durationMinutes"].apply(energy_level)

# Count trails by duration
print("
Trail Duration Breakdown:")
print(df["durationMinutes"].value_counts().sort_index())

# Count trails by energy level
counts = df["energyLevel"].value_counts()

# Create bar plot
plt.figure(figsize=(8, 6))
bars = plt.bar(counts.index, counts.values, color='steelblue')

# Add count labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 2, str(height),
             ha='center', va='bottom', fontsize=10)

# Customize axis labels and title
plt.title("Mood Breakdown", fontsize=14)
plt.xlabel("Mood", fontsize=12)
plt.ylabel("Number of Trails", fontsize=12)
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()