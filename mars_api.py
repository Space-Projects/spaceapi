import requests
import matplotlib.pyplot as plt
from datetime import datetime

with open('nasa.key', 'r') as file:
    KEY = file.read().rstrip()

def fetch_sunspot_data():
    url = f"https://api.nasa.gov/insight_weather/?api_key={KEY}&feedtype=json&ver=1.0"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

def plot_sunspot_data(data):
    if not data:
        return

    sol_keys = data["sol_keys"]
    sunspots = [data[str(sol)]["WD"]["most_common"]["compass_degrees"] for sol in sol_keys]
    dates = [datetime.strptime(data[str(sol)]["First_UTC"], "%Y-%m-%dT%H:%M:%S.%fZ") for sol in sol_keys]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, sunspots, marker="o", linestyle="-")
    plt.xlabel("Date")
    plt.ylabel("Sunspot Degrees")
    plt.title("Sunspot Data from NASA")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    data = fetch_sunspot_data()
    plot_sunspot_data(data)
