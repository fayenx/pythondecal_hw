#Question 1

import pandas as pd
df = pd.read_csv('global_air_quality.csv')
print(df)

df['PM25_Value'] = df['FactValueNumeric']
print(df[['FactValueNumeric', 'PM25_Value']])

continent_avg = df.groupby('ParentLocation')['PM25_Value'].mean().reset_index()
continent_avg.rename(columns={'PM25_Value': 'Average_PM25'}, inplace=True)
df = pd.merge(df, continent_avg, on='ParentLocation', how='left')
print(df[['Location', 'ParentLocation', 'PM25_Value', 'Average_PM25']])

max_avg = continent_avg.loc[continent_avg['Average_PM25'].idxmax()]
print(f"The continent with the highest average PM2.5 is {max_avg['ParentLocation']} with a value of {max_avg['Average_PM25']}.")
# This result is a little surprising to me, but I guess with more thought it makes sense as a 'developing' continent 

df[['Location', 'ParentLocation', 'PM25_Value', 'Average_PM25']].to_csv('processed_air_quality.csv', index=False)



# Question 2

import seaborn as sns
import matplotlib.pyplot as plt

planets = sns.load_dataset('planets')

plt.figure(figsize=(10, 6))
scatter = sns.scatterplot(
    data=planets, x='orbital_period', y='mass', hue='method', palette='viridis', alpha=0.7
)

plt.xscale('log')
plt.yscale('log')
plt.title('Exoplanets: Orbital Period vs Mass', fontsize=14)
plt.xlabel('Orbital Period (days)', fontsize=12)
plt.ylabel('Mass (Jupiter Mass)', fontsize=12)
plt.legend(title='Discovery Method', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

plt.show()


planets = planets.dropna(subset=['method', 'year'])
discovery_counts = planets.groupby(['year', 'method']).size().reset_index(name='count')
plt.figure(figsize=(14, 8))
bar = sns.barplot(
    data=discovery_counts, x='year', y='count', hue='method', dodge=False, palette='tab20'
)

plt.title('Exoplanets Discovered Per Year by Method', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Exoplanets Discovered', fontsize=12)
plt.legend(title='Discovery Method', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
