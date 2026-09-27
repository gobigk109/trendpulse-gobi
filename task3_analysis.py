
import pandas as pd

# Load cleaned data
df = pd.read_csv("cleaned_trending_data.csv")

# Find the highest scored story
top_story = df.loc[df["score"].idxmax()]

print("Top Trending Story:")
print(top_story["title"])
print("Score:", top_story["score"])

# Calculate average score
average_score = df["score"].mean()

print("Average Score:", average_score)

# Sort stories by score
df_sorted = df.sort_values("score", ascending=False)

print("\nStories sorted by score:")
print(df_sorted[["title", "score"]])
