from sqlalchemy import create_engine
import pandas as pd
import yaml
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)
    
cfg=config['PG']
print(cfg)

url = "{driver}://{user}:{password}@{host}/{database}".format(**cfg)
print('URL', url)

engine = create_engine(url)

# load with pandas 
names = pd.read_csv('https://datasets.imdbws.com/name.basics.tsv.gz', compression='gzip', sep='\t', nrows=1000)
title = pd.read_csv('https://datasets.imdbws.com/title.akas.tsv.gz', compression='gzip', sep='\t', nrows=1000)
basics = pd.read_csv('https://datasets.imdbws.com/title.basics.tsv.gz', compression='gzip', sep='\t', nrows=1000)
crew = pd.read_csv('https://datasets.imdbws.com/title.crew.tsv.gz', compression='gzip', sep='\t', nrows=1000)
episode = pd.read_csv('https://datasets.imdbws.com/title.episode.tsv.gz', compression='gzip', sep='\t', nrows=1000)
principals = pd.read_csv('https://datasets.imdbws.com/title.principals.tsv.gz', compression='gzip', sep='\t', nrows=1000)
ratings = pd.read_csv('https://datasets.imdbws.com/title.ratings.tsv.gz', compression='gzip', sep='\t', nrows=1000)

# sent data to database
names.to_sql('names', engine, if_exists='replace')
title.to_sql('title_akas', engine, if_exists='replace')
basics.to_sql('title_basics', engine, if_exists='replace')
crew.to_sql('title_crew', engine, if_exists='replace')
principals.to_sql('title_principals', engine, if_exists='replace')
ratings.to_sql('title_ratings', engine, if_exists='replace')
episode.to_sql('title_episode', engine, if_exists='replace')