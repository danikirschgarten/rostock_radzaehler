#%%
import pandas as pd
url = "https://www.hamburg-airport.de/service/flightdata/departures"
# %%
df = pd.read_json (url)
# %%
df
# %%
pivot = df.pivot_table(index="destinationAirportName", aggfunc="size")
pivot_sorted = pivot.sort_values(ascending=False)
# %%
pivot_sorted
# %%
