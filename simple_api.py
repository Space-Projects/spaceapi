import numpy as np
import matplotlib.pyplot as plt
import urllib.request
import pandas as pd


# Define the start and end dates
tstart = '2011/08'
tend = '2025/08'


# URL for sunspot data
url = "https://solarscience.msfc.nasa.gov/greenwch/spot_num.txt"

# Download data
urllib.request.urlretrieve(url, "sunspot_data.txt")

# Read the data from the text file
column_names = ["YEAR", "MONTH", "SSN", "DEV"]
data = pd.read_csv("sunspot_data.txt", delimiter="\s+", header=0)

# Convert YEAR and MONTH columns to a datetime object
data["DATE"] = pd.to_datetime(data["YEAR"].astype(str) + "-" + data["MON"].astype(str))

# Convert the date strings to datetime objects
start_date = pd.to_datetime(tstart)
end_date = pd.to_datetime(tend)

if start_date < min(data["DATE"]) or end_date > max(data["DATE"]):
    raise Exception("Date out of range. Must be within 1749/01 - 2015/04.")
# Filter the data based on the specified date range
filtered_data = data[(data["DATE"] >= start_date) & (data["DATE"] <= end_date)]

# Plot the sunspot data over time
plt.figure(figsize=(10, 5))
plt.plot(filtered_data["DATE"], filtered_data["SSN"], marker="o", linestyle="-")
plt.xlabel("Date")
plt.ylabel("Number of Sunspots")
plt.title(f"Sunspots Over Time: {tstart} to {tend}")
plt.grid()
plt.show()





