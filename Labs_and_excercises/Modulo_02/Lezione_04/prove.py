import pandas as pd

df = pd.read_csv('data.csv')
df = df[['Calories']].head(10)
print(df)
numero_giorni = 10
somma_tot = df.sum()
print(f'La somma delle calorie consumate nei primi {numero_giorni} giorni è: {somma_tot}')
media = df.mean()
print(f'La media delle calorie consumate nei primi {numero_giorni} giorni è: {media}')
# sm_tot = somma(df.head(numero_giorni))
