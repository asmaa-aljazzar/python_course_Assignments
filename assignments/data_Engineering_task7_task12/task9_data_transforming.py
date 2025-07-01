import pandas as pd

df = pd.read_csv('train.csv')

no_missing_row = df.dropna()

no_missing_row.info()

no_duplicate = df.drop_duplicates()

no_duplicate.info()

pclass_1 = df[df['Pclass'] == 1]

age_under_18 = df[df['Age'] < 18]

survived_name = df[df['Survived'] == 1]['Name']

pas_num_by_class = df['Pclass'].value_counts()

avg_age_by_class = df.groupby('Pclass')['Age'].mean()

pas_100_ticket = df[df['Fare'] > 100]

print(pclass_1)
print(age_under_18)
print(survived_name)
print(pas_100_ticket)
print(avg_age_by_class)
print(pas_num_by_class)