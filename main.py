import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('../Netflix/archive/raw_titles.csv').drop(['id', 'imdb_id'], axis=1).set_index('title')
df.info()

# MOVIES AND SHOW IMDB SCORE IN TIME
df_show_imdb = df[df['type'] == 'SHOW'].groupby('release_year').agg({'imdb_score': ['mean', 'count'], 'imdb_votes': 'sum'})
to_drop = df_show_imdb[df_show_imdb['imdb_score']['count'] < 5].index # Dropping years with less than 5 shows
df_show_imdb.drop(to_drop, inplace=True)

df_imdb = df[df['type'] == 'MOVIE'].groupby('release_year').agg({'imdb_score': ['mean', 'count'], 'imdb_votes': 'sum'})
to_drop = df_imdb[df_imdb['imdb_score']['count'] < 5].index # Dropping years with less than 5 movies
df_imdb.drop(to_drop, inplace=True)

df_imdb['imdb_score']['mean'].plot(linewidth=0.1, marker='.', legend=True, label='MOVIE score', color='g')
df_imdb['imdb_score']['count'].plot(secondary_y=True, linewidth=0.1, linestyle='--', marker='', markersize=3, legend=True, label='MOVIE counter', color='g')
df_show_imdb['imdb_score']['mean'].plot(linewidth=0.1, marker='.', legend=True, label='SHOW score', color='r')
df_show_imdb['imdb_score']['count'].plot(secondary_y=True, linewidth=0.1, linestyle='--', marker='', markersize=3, legend=True, label='SHOW counter', color='r')
plt.title('Average IMDB score and number of movies/shows in years')
plt.show()

# MOVIES RUNTIME LENGTH
df_runt = df[df['type']=='MOVIE'].groupby('release_year').agg({'runtime': ['mean', 'max', 'min', 'count', 'std']})
to_drop = df_runt[df_runt['runtime']['count'] < 5].index # Dropping years with less than 5 movies
df_runt.drop(to_drop, inplace=True)
df_runt
plt.plot(df['release_year'], df['runtime'], linewidth=0, marker='.')
plt.plot(df_runt.index, df_runt['runtime']['mean'])
plt.legend(labels=['sepeate movies', 'average for year'])
plt.title('Length of movies in time')
plt.show()