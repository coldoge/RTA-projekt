import pandas as pd
import re

df = pd.read_csv('data/audi_a6_1000obs.csv', index_col=0, dtype=str)

print(df.isna().sum(axis=0))

# wyrzucamy zmienne z wieloma brakami danych
cols = list(df.loc[:, :'Kolor'].columns) + ['Stan']

# wyrzucamy zmienne z brakami danych oraz zmienne, ktore uwazamy za nieistotne
for zmienna in ['Kategoria', 'Marka pojazdu', 'Model pojazdu', 'Liczba drzwi', 'Liczba miejsc', 'Wersja',
                'Spalanie W Mieście']:
    cols.remove(zmienna)

# wyrzucamy wiersze z brakami danych
df = df[cols].dropna(axis=0)


def extract_number_from_string(napis):
    return int(re.search('[\d ]+', napis).group(0).replace(' ', ''))


for zmienna in ['Cena', 'Rok produkcji', 'Przebieg', 'Pojemność skokowa', 'Moc']:
    df[zmienna] = df[zmienna].apply(extract_number_from_string)

for i in df.columns:
    print(df[i].value_counts())

# wyrzucamy obserwacje kategoryczne z licznoscia mniejsza od 5

df = df[~df['Napęd'].isin(['Na tylne koła', '4x4 (dołączany ręcznie)'])]
df = df[~df['Typ nadwozia'].isin(['SUV', 'Kompakt'])]
df = df[df['Kolor'] != 'Bordowy']

# wyrzucamy nietypowe/bledne obserwacje

df = df[df['Moc'] != 1]

df = df.reset_index(drop=True)
df['wiek'] = 2022 - df['Rok produkcji']
df.to_csv('data/final_audi_a6_data.csv')

