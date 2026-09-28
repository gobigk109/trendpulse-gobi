import pandas as pd
import numpy as np

df = pd.read_csv("data/trends_clean.csv")
print(df.head())
print("Shape:", df.shape)
print("Average score:", df["score"].mean())
print("Average comments:", df["num_comments"].mean())
scores = df["score"].to_numpy()

print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
print("Standard deviation:", np.std(scores))
print("Highest score:", np.max(scores))
print("Lowest score:", np.min(scores))
category_counts = df["category"].value_counts()

print("Category counts:")
print(category_counts)

print("Category with most stories:", category_counts.idxmax())
max_comments = df["num_comments"].idxmax()

print("Story with most comments:", df.loc[max_comments, "title"])
print("Comment count:", df.loc[max_comments, "num_comments"])
