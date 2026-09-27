
import requests
import pandas as pd

# Get live trending story IDs
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(url)

top_stories = response.json()

# Collect story details
stories = []

for story_id in top_stories[:10]:
    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    data = requests.get(story_url).json()

    if data:
        stories.append(data)

# Convert to DataFrame
df = pd.DataFrame(stories)

# Keep required columns
df = df[["title", "score", "by"]]

# Save raw collected data
df.to_csv("trending_data.csv", index=False)

print("Task 1 completed successfully!")
print("Stories collected:", len(df))
