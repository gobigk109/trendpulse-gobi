
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("cleaned_trending_data.csv")

# Sort by score
df_sorted = df.sort_values("score", ascending=False)

# Bar chart
plt.figure(figsize=(10, 6))

plt.bar(df_sorted["title"], df_sorted["score"])

plt.xlabel("Trending Stories")
plt.ylabel("Score")
plt.title("Trending Stories by Score")

plt.xticks(rotation=90)
plt.tight_layout()

plt.savefig("trending_scores.png")
plt.show()

# Score distribution
plt.figure(figsize=(8, 5))

plt.hist(df["score"], bins=5)

plt.xlabel("Score")
plt.ylabel("Number of Stories")
plt.title("Distribution of Trending Story Scores")

plt.tight_layout()

plt.savefig("score_distribution.png")
plt.show()

print("Task 4 completed successfully!")
