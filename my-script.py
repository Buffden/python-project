import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
dataset = pd.read_csv("./datasets/England 2 CSV.csv")

# Show first 5 rows
print(dataset.head())

# Show column names
print(dataset.columns)

# Check for missing values
print(dataset.isnull().sum())

# Drop unnecessary columns (modify as needed)
dataset = dataset.drop(["Referee", "League"], axis=1)

# Rename columns for readability
dataset = dataset.rename(columns={"FTHG": "HomeGoals", "FTAG": "AwayGoals", "FTR": "Result"})

# Convert date column to datetime format
dataset["Date"] = pd.to_datetime(dataset["Date"])

# Show dataset summary
print("Dataset Info:")
print(dataset.info())

# Show basic statistics
print("\nBasic Statistics:")
print(dataset.describe())

# Check for missing values
print("\nMissing Values:")
print(dataset.isnull().sum())


print(dataset.head())


# after running the EDA we want to do some changes to refine or clean the data:

dataset.columns = dataset.columns.str.replace(" ", "_")

# Fill missing numerical values with mean
dataset.fillna(dataset.mean(numeric_only=True), inplace=True)

#since there is missmatch in date format we need to convert it to a single format i.e. dd/mm/yyyy but Pandas assumes MM/DD/YYYY.
dataset["Date"] = pd.to_datetime(dataset["Date"], format="%d/%m/%Y", errors="coerce")

# Now lets visualize the data in charts: its fun :)
print("Dataset columns:")
print(dataset.columns)


# Rename columns for consistency
dataset.rename(columns={
    "FTH_Goals": "HomeGoals",
    "FTA_Goals": "AwayGoals"
}, inplace=True)

# Group by Season and calculate average goals per season
goals_per_season = dataset.groupby("Season")[["HomeGoals", "AwayGoals"]].mean()

# Plot the trend of average home and away goals per season
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(goals_per_season.index, goals_per_season["HomeGoals"], marker="o", label="Home Goals", color="blue")
plt.plot(goals_per_season.index, goals_per_season["AwayGoals"], marker="o", label="Away Goals", color="red")
plt.title("Average Goals Per Season (Home vs Away)")
plt.xlabel("Season")
plt.ylabel("Average Goals")
plt.legend()
plt.grid(True)
plt.show()

sns.countplot(x="FT_Result", data=dataset, palette="Set2")
plt.title("Distribution of Match Results (H = Home Win, A = Away Win, D = Draw)")
plt.show()