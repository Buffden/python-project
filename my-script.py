import pandas as pd

# Load dataset
df = pd.read_csv("./datasets/England 2 CSV.csv")

# Show first 5 rows
print(df.head())

# Show column names
print(df.columns)

# Check for missing values
print(df.isnull().sum())

# Drop unnecessary columns (modify as needed)
df = df.drop(["Referee", "Notes"], axis=1)

# Rename columns for readability
df = df.rename(columns={"FTHG": "HomeGoals", "FTAG": "AwayGoals", "FTR": "Result"})

# Convert date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

print(df.head())
