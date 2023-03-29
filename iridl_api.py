import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from netCDF4 import Dataset, num2date
import requests
from io import BytesIO

def get_nearest_index(array, value):
    return (np.abs(array - value)).argmin()

def plot_temperature(longitude, latitude, altitude):
    # Download the latest dataset
    url = "http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP/.CPC/.GHCN_CAMS/.gridded/.deg0p5/.temp/dods"
    response = requests.get(url)
    response.raise_for_status()

# http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP/.CPC/.GHCN_CAMS/.gridded/.deg0p5/.temp/
    # Read the dataset
    nc_file = BytesIO(response.content)
    dataset = Dataset(nc_file)

    # Get the required variables
    time_var = dataset.variables['T']
    lat_var = dataset.variables['Y']
    lon_var = dataset.variables['X']
    alt_var = dataset.variables['Z']
    temp_var = dataset.variables['temp']

    # Find the nearest indices for the given latitude, longitude, and altitude
    lat_idx = get_nearest_index(lat_var[:], latitude)
    lon_idx = get_nearest_index(lon_var[:], longitude)
    alt_idx = get_nearest_index(alt_var[:], altitude)

    # Fetch the temperature data for the specified location
    temp_data = temp_var[:, alt_idx, lat_idx, lon_idx]

    # Convert the time variable to dates
    dates = num2date(time_var[:], time_var.units)

    # Create a DataFrame and plot the data
    df = pd.DataFrame(data={'Temperature': temp_data, 'Date': dates})
    df.set_index('Date', inplace=True)
    df.plot(title=f"Temperature at {latitude}°N, {longitude}°E, {altitude}m", ylabel="Temperature (°C)")

    plt.show()

if __name__ == "__main__":
    longitude = 75.0
    latitude = 20.0
    altitude = 1000

    plot_temperature(longitude, latitude, altitude)
