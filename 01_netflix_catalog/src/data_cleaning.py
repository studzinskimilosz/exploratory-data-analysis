import pandas as pd
import numpy as np

df = pd.read_csv("../data/netflix_titles.csv")

### Description
print(df.info())
print(df.describe())

### Missing values
na_values = df.isnull().sum()
percentage_na = na_values * 100 / len(df)

missing_values = {
    'Missing numbers': na_values.sort_values(ascending=False),
    'Missing percentage': percentage_na.sort_values(ascending=False)
}

print(missing_values)

### Duplicates

print(df.duplicated().sum()) #no duplicates

### Text columns
print(df.columns)

text_columns = ['type', 'type', 'title', 'director', 'cast', 'country', 'rating', 'duration', 'listed_in', 'description']

for col in text_columns:
    df[col] = df[col].str.strip().str.lower().str.replace(' ', '_')

### Date
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

df["year_added"] = df["date_added"].dt.year
df["month_added"] = df["date_added"].dt.month
df["month_name_added"] = df["date_added"].dt.month_name()

df['age_of_show'] = df['year_added'] - df['release_year']

df['age_of_show'].describe()

### Negative values
col_to_check = ['title', 'release_year', 'date_added', 'year_added', 'age_of_show']

negavite_check = df.loc[df['age_of_show'] < 0, col_to_check]

## Handling this values
df.loc[df['age_of_show'] < 0, 'age_of_show'] = np.nan

### Time handling
df['duration_value'] = df['duration'].str.extract(r'(\d+)', expand=False)
df['duration_value'] = pd.to_numeric(df['duration_value'], errors='coerce')

# print(df['type'].unique())
df['movie_duration_min'] = np.where(df['type'] =='movie', df['duration_value'], np.nan)
df['tv_seasons'] = np.where(df['type'] =='tv_Show', df['duration_value'], np.nan)

