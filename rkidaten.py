#%%
#zuerst pandas installieren
# %%
import pandas as pd
# %%
url = "https://github.com/robert-koch-institut/SARS-CoV-2-Infektionen_in_Deutschland/raw/refs/heads/main/Aktuell_Deutschland_SarsCov2_Infektionen.csv?download="
# %%
df = pd.read_csv (url)
# %%
df
# %%
#wir filtern den Landkreis, in diesem Fall Kiel
df_kiel = df [df ["IdLandkreis"] == 1002]
df_kiel
# %%
#Summe Infektionen Kiel
df_kiel["AnzahlFall"].sum()
# %%
df_kiel["AnzahlTodesfall"].sum()
# %%
df_kiel_faelle = df_kiel.pivot_table(index="Meldedatum", values= ["AnzahlFall", "AnzahlTodesfall"], aggfunc="sum")
df_kiel_faelle
df_kiel_faelle.to_csv("faelle_kiel.csv")
# %%
df_traunstein = df [df ["IdLandkreis"] == 9189]
df_traunstein.pivot_table (index="Geschlecht", values="AnzahlTodesfall", aggfunc="sum")
# %%
