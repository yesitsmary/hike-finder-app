import matplotlib.pyplot as plt
import re

# Convert trail durations to minutes
def duration_to_minutes(duration):
    duration = str(duration).strip().lower()

    # Normalize different dash characters
    duration = duration.replace("–", "-")

    # Common keywords
    if "half day" in duration:
        return 360
    if "full day" in duration:
        return 720
    if "2-3 days" in duration or "1-3 days" in duration:
        return 1440 * 2.5  # average of 2–3 days
    if "days" in duration:
        return 1440  # 1 day default if unspecified

    # Match ranges like "1-2 Hours", "30-60 Minutes"
    match = re.match(r"(\d+)\s*-\s*(\d+)\s*(minutes|minute|hours|hour)", duration)
    if match:
        low, high, unit = match.groups()
        avg = (int(low) + int(high)) / 2
        return avg * 60 if "hour" in unit else avg

    # Match exact time like "45 minutes", "2 hours"
    match = re.match(r"(\d+)\s*(minutes|minute|hours|hour)", duration)
    if match:
        val, unit = match.groups()
        return int(val) * 60 if "hour" in unit else int(val)

    return None  # Fallback if format doesn't match