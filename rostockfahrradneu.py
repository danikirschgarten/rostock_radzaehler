#%%
import requests
#%%
import io
# %%
url = "https://geo.sv.rostock.de/download/opendata/radmonitore/radmonitore_daten.csv"
response = requests.get(url, verify=True)
df = pd.read_csv(io.StringIO(response.text))
# %%
df['zeitpunkt'] = pd.to_datetime(df['zeitpunkt'], utc=True)
