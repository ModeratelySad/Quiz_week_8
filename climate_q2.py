import matplotlib.pyplot as plt
import pandas as pd

# Load data from the CSV file
data = pd.read_csv('climate.csv')  # Replace 'climate.csv' with the actual file path

# Extract years, CO2, and temperature data from the DataFrame
years = data['Year']
co2 = data['CO2']
temp = data['Temperature']

# Create the figure and subplots
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")

plt.tight_layout()  # Ensures that the subplots do not overlap
plt.savefig("co2_temp_2.png")
plt.show()
