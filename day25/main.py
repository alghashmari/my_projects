import pandas as pd

# Load the dataset
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Count squirrels by fur color
gray_count = data["Primary Fur Color"].value_counts().get("Gray", 0)
cinnamon_count = data["Primary Fur Color"].value_counts().get("Cinnamon", 0)
black_count = data["Primary Fur Color"].value_counts().get("Black", 0)

# Create a dictionary for fur color counts
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

# Convert the dictionary to a DataFrame
squirrel_count_df = pd.DataFrame(data_dict)

# Save the DataFrame to a CSV file
squirrel_count_df.to_csv("squirrel_count.csv", index=False)
# Print confirmation
print("squirrel_count.csv has been created successfully!")