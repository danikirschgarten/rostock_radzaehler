#%%

import datetime
import pandas as pd
from datetime import datetime, timedelta
# %%
url = "https://www.ostsee.de/kiel/kreuzfahrtschiffe.php#liste"
df = pd.read_html(url) [-1]
print (df)
# %%
#Datenangaben in maschinenlesbares Datum umwandeln
df['ankunft_maschine'] = pd.to_datetime(df['Ankunft'].str.extract(r'(\d{2}\.\d{2}\.\d{4})')[0],
    format='%d.%m.%Y')
# %%
# %%
#die Ankunften der nächsten fünf Tage anzeigen
df.sort_values(by="ankunft_maschine", ascending=True)
# %%
heute = datetime.today().date()
# Enddatum = heute + 4 Tage
enddatum = heute + timedelta(days=4)
# Filtern des DataFrames
df_aktuell = df[
    (df['ankunft_maschine'].dt.date >= heute) &
    (df['ankunft_maschine'].dt.date <= enddatum)]
# %%
df_aktuell.to_csv ("kiel_kreuzfahrt.csv")
# %%
