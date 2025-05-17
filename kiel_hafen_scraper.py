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
df.iloc[0]
# %%
pivot = df.pivot_table(index="Schiffsname", aggfunc="size")
pivot_sorted = pivot.sort_values(ascending=False)
print(pivot_sorted.head(1))
# %%
df.sort_values(by="Länge", ascending=False)
# %%

# Spalten anzeigen
print("Verfügbare Spalten:", df.columns.tolist())

# Nimm an, dass die Schiffe in der ersten Spalte sind
# Falls nicht, passe dies entsprechend an
schiff_spalte = df.columns[1]

# Häufigkeit der Schiffe zählen
schiff_counts = df[schiff_spalte].value_counts()

# Das häufigste Schiff finden
haeufigste_schiff = schiff_counts.idxmax()
anzahl_ankuenfte = schiff_counts.max()

print(f"\nDas häufigste Schiff in Kiel ist: {haeufigste_schiff}")
print(f"Anzahl der Ankünfte: {anzahl_ankuenfte}")
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
df_aktuell
# %%
