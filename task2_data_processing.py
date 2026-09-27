
import pandas as pd

# Load collected data
df = pd.read_csv("trending_data.csv")

# Check for missing values
print("Missing values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Clean title text
df["title"] = df["title"].str.strip()

# Make sure score is numeric
df["score"] = pd.to_numeric(df["score"], errors="coerce")

# Remove rows with missing score
df = df.dropna(subset=["score"])

# Save cleaned data
df.to_csv("cleaned_trending_data.csv", index=False)

print("Task 2 completed successfully!")
print("Rows after cleaning:", len(df))
