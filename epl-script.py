import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn as sns
import matplotlib.pyplot as plt

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

# Convert date column to datetime format
dataset["Date"] = pd.to_datetime(dataset["Date"])

# Show dataset summary
print("Dataset Info:")
print(dataset.info())

# Show basic statistics
print("\nBasic Statistics:")
print(dataset.describe())

# after running the EDA we want to do some changes to refine or clean the data:

dataset.columns = dataset.columns.str.replace(" ", "_")

# Fill missing numerical values with mean
# Reason: The mean is a better measure of central tendency for continuous data
dataset.fillna(dataset.mean(numeric_only=True), inplace=True)

#since there is missmatch in date format we need to convert it to a single format i.e. dd/mm/yyyy but Pandas assumes MM/DD/YYYY.
dataset["Date"] = pd.to_datetime(dataset["Date"], format="%d/%m/%Y", errors="coerce")

# Now lets visualize the data in charts: its fun :)

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

# total goals per season trends


# Calculate total goals per season
dataset["TotalGoals"] = dataset["HomeGoals"] + dataset["AwayGoals"]
goals_per_season = dataset.groupby("Season")["TotalGoals"].mean()

# Plot average goals per season
plt.figure(figsize=(12, 6))
plt.plot(goals_per_season.index, goals_per_season.values, marker="o", linestyle="-", color="green")
plt.title("Average Goals Per Season")
plt.xlabel("Season")
plt.ylabel("Average Goals Per Match")
plt.grid(True)
plt.show()


# To see how home advantage has changed, let’s calculate win percentages for each season.
# Calculate win percentages
win_counts = dataset.groupby(["Season", "FT_Result"]).size().unstack()
win_percentage = win_counts.div(win_counts.sum(axis=1), axis=0) * 100

# Plot home, away, and draw trends over seasons
plt.figure(figsize=(12, 6))
win_percentage.plot(kind="line", marker="o", ax=plt.gca())
plt.title("Win Percentage Trends Over Seasons")
plt.xlabel("Season")
plt.ylabel("Percentage of Matches")
plt.legend(title="Result")
plt.grid(True)
plt.show()
