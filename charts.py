import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



df = pd.read_csv('data/final_audi_a6_data.csv')

df.drop(df.filter(regex="Unname"), axis=1, inplace=True)

# In[93]:


kolumny = list(df.columns)
print(kolumny)

# In[97]:


licz_of = df['Oferta od'].value_counts()
plt.pie(licz_of, autopct='%1.1f%%', startangle=180)
plt.title('Kto wystawił samochód')
plt.legend(labels=['Osoba prywatna', 'Firma'], loc=1)
# In[91]:


sns.histplot(df.Cena, color='red')
plt.xlabel('Cena')
plt.ylabel('Ilość samochodów')
plt.title('Histogram Ceny')
plt.show()
# In[107]:


lata = df['Rok produkcji'].value_counts()
plt.figure(figsize=(12, 6))
plt.xticks(rotation=75)
plt.title('Wykres słupkowy roku produkcji')
sns.set_style('darkgrid')
sns.barplot(x=lata.index, y=lata)
plt.ylabel('Ilość samochodów')

# In[98]:


sns.histplot(df.Przebieg, color='red')
plt.xlabel('Przebieg')
plt.ylabel('Ilość samochodów')
plt.title('Histogram Przebiegu')

# In[116]:


sns.histplot(df['Pojemność skokowa'], bins=10, color='red')
plt.xlabel('Pojemność skokowa')
plt.ylabel('Ilość samochodów')
plt.title('Histogram Pojemności skokowej')

# In[124]:


licz_of = df['Rodzaj paliwa'].value_counts()
plt.pie(licz_of, startangle=180)
plt.title('Rodzaj paliwa')
plt.legend(labels=licz_of.index, loc=1)

# In[126]:


lata = df['Moc'].value_counts()
plt.figure(figsize=(12, 6))
plt.xticks(rotation=75)
plt.title('Wykres słupkowy mocy')
sns.set_style('darkgrid')
sns.barplot(x=lata.index, y=lata)
plt.ylabel('Ilość samochodów')

# In[130]:


sns.histplot(df['Moc'], bins=50, color='red')
plt.xlabel('Moc silnika')
plt.ylabel('Ilość samochodów')
plt.title('Histogram Mocy')

# In[137]:


skrzynia = df['Skrzynia biegów'].value_counts()
plt.pie(skrzynia, autopct='%1.1f%%', startangle=180)
plt.title('Rodzaj skrzyni biegów')
plt.legend(labels=skrzynia.index, loc=1)

# In[142]:


nap = df['Napęd'].value_counts()
plt.pie(nap, autopct='%1.1f%%', startangle=180)
plt.title('Rodzaj napędu')
plt.legend(labels=nap.index, loc=1)

# In[144]:


nad = df['Typ nadwozia'].value_counts()
plt.pie(nad, autopct='%1.1f%%', startangle=180)
plt.title('Typ nadwozia')
plt.legend(labels=nad.index, loc=1)

# In[146]:


kolor = df['Kolor'].value_counts()
plt.figure(figsize=(12, 6))
plt.xticks(rotation=75)
plt.title('Wykres słupkowy koloru')
sns.set_style('darkgrid')
sns.barplot(x=kolor.index, y=kolor)
plt.ylabel('Ilość samochodów')

# In[147]:


stan = df['Stan'].value_counts()
plt.pie(stan, autopct='%1.1f%%', startangle=180)
plt.title('Stan')
plt.legend(labels=stan.index, loc=1)

# In[170]:


fig, axes = plt.subplots(2, 3, figsize=(16, 8))
licz_of = df['Oferta od'].value_counts()
licz_pal = df['Rodzaj paliwa'].value_counts()
skrzynia = df['Skrzynia biegów'].value_counts()
nap = df['Napęd'].value_counts()
stan = df['Stan'].value_counts()
nad = df['Typ nadwozia'].value_counts()

axes[0, 0].pie(licz_of, autopct='%1.1f%%', startangle=180)
axes[0, 0].set_title('Kto wystawił samochód')
axes[0, 0].legend(labels=['Osoba prywatna', 'Firma'], loc=1)

axes[0, 1].pie(licz_pal, startangle=180)
axes[0, 1].set_title('Rodzaj paliwa')
axes[0, 1].legend(labels=licz_pal.index, loc=2, ncol=2)

axes[0, 2].pie(skrzynia, autopct='%1.1f%%', startangle=180)
axes[0, 2].set_title('Rodzaj skrzyni biegów')
axes[0, 2].legend(labels=skrzynia.index, loc=1)

axes[1, 0].pie(nap, autopct='%1.1f%%', startangle=180)
axes[1, 0].set_title('Rodzaj napędu')
axes[1, 0].legend(labels=nap.index, loc=1)

axes[1, 1].pie(nad, autopct='%1.1f%%', startangle=180)
axes[1, 1].set_title('Typ nadwozia')
axes[1, 1].legend(labels=nad.index, loc=1)

axes[1, 2].pie(stan, autopct='%1.1f%%', startangle=180)
axes[1, 2].set_title('Stan')
axes[1, 2].legend(labels=stan.index, loc=1)

# In[176]:


fig, axes = plt.subplots(2, 2, figsize=(16, 8))

sns.histplot(df.Cena, color='red', ax=axes[0, 0])
axes[0, 0].set_xlabel('Cena')
axes[0, 0].set_ylabel('Ilość samochodów')
axes[0, 0].set_title('Histogram Ceny')

sns.histplot(df.Przebieg, color='blue', ax=axes[0, 1])
axes[0, 1].set_xlabel('Przebieg')
axes[0, 1].set_ylabel('Ilość samochodów')
axes[0, 1].set_title('Histogram Przebiegu')

sns.histplot(df['Pojemność skokowa'], bins=10, color='green', ax=axes[1, 0])
axes[1, 0].set_xlabel('Pojemność skokowa')
axes[1, 0].set_ylabel('Ilość samochodów')
axes[1, 0].set_title('Histogram Pojemności skokowej')

sns.histplot(df['Moc'], bins=50, color='orange', ax=axes[1, 1])
axes[1, 1].set_xlabel('Moc silnika')
axes[1, 1].set_ylabel('Ilość samochodów')
axes[1, 1].set_title('Histogram Mocy')

plt.tight_layout(pad=2)

# In[194]:


fig, axes = plt.subplots(3, 1, figsize=(16, 8))
sns.set_style('darkgrid')

lata = df['Rok produkcji'].value_counts()
moc = df['Moc'].value_counts()
kolor = df['Kolor'].value_counts()

axes[0].set_title('Wykres słupkowy roku produkcji')
sns.barplot(x=lata.index, y=lata, ax=axes[0])
axes[0].set_ylabel('Ilość samochodów')
for tick in axes[0].get_xticklabels():
    tick.set_rotation(75)

axes[1].set_title('Wykres słupkowy mocy')
sns.barplot(x=moc.index, y=moc, ax=axes[1])
axes[1].set_ylabel('Ilość samochodów')
for tick in axes[1].get_xticklabels():
    tick.set_rotation(75)

axes[2].set_title('Wykres słupkowy koloru')
sns.barplot(x=kolor.index, y=kolor, ax=axes[2])
axes[2].set_ylabel('Ilość samochodów')
for tick in axes[2].get_xticklabels():
    tick.set_rotation(75)

plt.tight_layout(pad=2)

# In[197]:


fig, axes = plt.subplots(1, 3, figsize=(16, 8))

sns.scatterplot(x='Przebieg', y='Cena', hue='Oferta od', data=df, ax=axes[0])
axes[0].set_xlabel("Przebieg")
axes[0].set_ylabel("Cena")

sns.scatterplot(x='Przebieg', y='Cena', hue='Skrzynia biegów', data=df, ax=axes[1])
axes[1].set_xlabel("Przebieg")
axes[1].set_ylabel("Cena")

sns.scatterplot(x='Przebieg', y='Cena', hue='Napęd', data=df, ax=axes[2])
axes[2].set_xlabel("Przebieg")
axes[2].set_ylabel("Cena")

# In[198]:


fig, axes = plt.subplots(1, 3, figsize=(16, 8))

sns.scatterplot(x='Rok produkcji', y='Cena', hue='Oferta od', data=df, ax=axes[0])
axes[0].set_xlabel("Rok produkcji")
axes[0].set_ylabel("Cena")

sns.scatterplot(x='Rok produkcji', y='Cena', hue='Skrzynia biegów', data=df, ax=axes[1])
axes[1].set_xlabel("Rok produkcji")
axes[1].set_ylabel("Cena")

sns.scatterplot(x='Rok produkcji', y='Cena', hue='Napęd', data=df, ax=axes[2])
axes[2].set_xlabel("Rok produkcji")
axes[2].set_ylabel("Cena")

# In[199]:


fig, axes = plt.subplots(1, 3, figsize=(16, 8))

sns.scatterplot(x='Moc', y='Cena', hue='Oferta od', data=df, ax=axes[0])
axes[0].set_xlabel("Moc")
axes[0].set_ylabel("Cena")

sns.scatterplot(x='Moc', y='Cena', hue='Skrzynia biegów', data=df, ax=axes[1])
axes[1].set_xlabel("Moc")
axes[1].set_ylabel("Cena")

sns.scatterplot(x='Moc', y='Cena', hue='Napęd', data=df, ax=axes[2])
axes[2].set_xlabel("Moc")
axes[2].set_ylabel("Cena")

# In[200]:


fig, axes = plt.subplots(1, 3, figsize=(16, 8))

sns.scatterplot(x='Pojemność skokowa', y='Cena', hue='Oferta od', data=df, ax=axes[0])
axes[0].set_xlabel("Pojemność skokowa")
axes[0].set_ylabel("Cena")

sns.scatterplot(x='Pojemność skokowa', y='Cena', hue='Skrzynia biegów', data=df, ax=axes[1])
axes[1].set_xlabel("Pojemność skokowa")
axes[1].set_ylabel("Cena")

sns.scatterplot(x='Pojemność skokowa', y='Cena', hue='Napęd', data=df, ax=axes[2])
axes[2].set_xlabel("Pojemność skokowa")
axes[2].set_ylabel("Cena")

# In[201]:


fig, axes = plt.subplots(1, 2, figsize=(16, 8))

sns.scatterplot(x='Przebieg', y='Cena', hue='Typ nadwozia', data=df, ax=axes[0])
axes[0].set_xlabel("Przebieg")
axes[0].set_ylabel("Cena")

sns.scatterplot(x='Rok produkcji', y='Cena', hue='Typ nadwozia', data=df, ax=axes[1])
axes[1].set_xlabel("Rok produkcji")
axes[1].set_ylabel("Cena")

# In[85]:


df

