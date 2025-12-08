import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather.csv")

# the first few rows
print("Here is what the dataset looks like:")
print(df.head())
print("\n")



# Here, I make a line graph to show how temperature changes over months

plt.figure(figsize=(8, 5))

plt.plot(df["Month"], df["AverageTemp"], marker="o", linewidth=2)
# marker="o" puts dots on each data point to make it easier to see.
# Customizations like this you can find on w3schools or online

plt.title("Average Temperature by Month")
plt.xlabel("Month")
plt.ylabel("Temperature (°F)")

plt.grid(True)  # I did this to make it easier to read
plt.tight_layout()
plt.savefig("temp_line_plot.png")
plt.show()


# Here I make a bar graph that compares two different cities on the same graph

plt.figure(figsize=(8, 5))

# Two bars for each month: one for NYC, one for LA
plt.bar(df["Month"], df["RainNYC"], alpha=0.7, label="NYC Rainfall")
plt.bar(df["Month"], df["RainLA"], alpha=0.7, label="LA Rainfall")

plt.title("Rainfall Comparison: NYC vs LA")
plt.xlabel("Month")
plt.ylabel("Rainfall (inches)")
plt.legend()  # this method adds a legend which explains the two data sources

plt.tight_layout()
plt.savefig("rain_bar_plot.png")
plt.show()
