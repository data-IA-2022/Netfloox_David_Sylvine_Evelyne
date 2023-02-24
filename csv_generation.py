import pandas as pd
import numpy as np
from sqlalchemy import create_engine, types
import os, yaml # credentials:
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Récup des info de connection
with open('config_local.yaml', 'r') as file:
    config = yaml.safe_load(file)
#print(config)

cfg=config['PG']
print(cfg)

# Connection à BDD
url = "{driver}://{user}:{password}@{host}/{database}".format(**cfg)
print('URL', url)
engine = create_engine(url)

df = pd.read_sql("""SELECT A.tconst, "primaryTitle", "isAdult", decade, "runtimeMinutes", genres, nconst, "averageRating", "numVotes" FROM basics_knownForTitles A INNER JOIN title_ratings B ON (A.tconst=B.tconst);""", engine)

df.to_csv('basics_knownForTitles_ratings.csv')
