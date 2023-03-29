import datetime
import numpy as np
import matplotlib.pyplot as plt
from pyglow import pyglow

def fetch_iri_temperature_data(lat, lon, alt, start_time, end_time, time_step):
    time_profiles = []
    time_values = []

    current_time = start_time
    while current_time <= end_time:
        pt = pyglow.Point(current_time, lat, lon, alt)
        pt.run_iri()
        temperature = pt.Te
        time_profiles.append(temperature)
        time_values.append(current_time)
        current_time += datetime.timedelta(minutes=time_step)

    return time_values, time_profiles

def plot_iri_temperature(lat, lon, alt, start_time, end_time, time_step):
    time_values, temperature_profiles = fetch_iri_temperature_data(lat, lon, alt, start_time, end_time, time_step)
    plt.plot(time_values, temperature_profiles)
    plt.xlabel('Time')
    plt.ylabel('Temperature (K)')
    plt.title(f'Temperature at {lat}N, {lon}E, {alt}km altitude')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    lat = 40.7128  # Latitude (degrees)
    lon = -74.0060  # Longitude (degrees)
    alt = 100       # Altitude (km)

    start_time = datetime.datetime.now() - datetime.timedelta(hours=1)
    end_time = datetime.datetime.now()
    time_step = 10  # Time step in minutes

    plot_iri_temperature(lat, lon, alt, start_time, end_time, time_step)
