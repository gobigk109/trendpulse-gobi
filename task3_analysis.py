import pandas as pd
import numpy as np

df = pd.read_csv("data/trends_clean.csv")
print(df.head())
print("Shape:", df.shape)
print("Average score:", df["score"].mean())
print("Average comments:", df["num_comments"].mean())
