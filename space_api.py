import matplotlib.pyplot as plt
import sunpy.map
from sunpy.net import Fido, attrs as a
from datetime import datetime, timedelta

# Set the time range for sunspot data
# now = datetime.utcnow()
# start_time = now - timedelta(days=365)

tstart = '2011/08/09 07:23:56'
tend = '2012/08/09 12:40:29'

# Query the HEK for sunspot data within the specified time range
result = Fido.search(a.Time(tstart, tend),
                     a.hek.EventType("SS"))
# ,
#                      a.hek.OBS.Observatory == "SDO",
#                      a.hek.OBS.Instrument == "HMI")

# result = Fido.search(a.Time(tstart,tend), a.hek.EventType("FL")) #SOLAR FLARE

# Download sunspot data
if len(result) > 0:
    sunspot_data = Fido.fetch(result[0])

# Load sunspot data into a SunPy Map
if sunspot_data:
    sunspot_map = sunpy.map.Map(sunspot_data)

# Plot sunspot data
if sunspot_data:
    fig = plt.figure()
    ax = plt.subplot(projection=sunspot_map)
    sunspot_map.plot()
    sunspot_map.draw_limb()
    ax.set_title(f"Sunspot Data from NASA's HEK - {start_time} to {now}")
    plt.show()
else:
    print("No sunspot data found within the specified time range.")

