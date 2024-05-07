import pandas as pd

df = pd.read_csv('data.csv')
numero_giorni = int(input("Inserisci il numero dei giorni con quali vuoi lavorare: "))
df = df[['Calories']].head(numero_giorni)
print(f'I dati che sto usando sono i seguenti:\n\n{df}')
somma_tot = round(df.sum()).to_string()
print(f'\nLa somma delle calorie consumate nei primi {numero_giorni} giorni è: {somma_tot}')
media = round(df.mean()).to_string()
print(f'La media delle calorie consumate nei primi {numero_giorni} giorni è: {media}')
