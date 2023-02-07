from sqlalchemy import create_engine
import pandas as pd
'''
with open("config.yml") as file:
    
host="greta-p2-g2.westeurope.cloudapp.azure.com"

pgSQLengine = create_engine(
"postgresql+psycopg2://%s:%s@%s/%s" %
("postgres", "greta2023", host, 'test'))

df = pd.read_csv('https://datasets.imdbws.com/name.basics.tsv.gz', compression='gzip', sep='\t', nrows=10)
df.to_sql('test_names', pgSQLengine)
'''

names = pd.read_csv('https://datasets.imdbws.com/name.basics.tsv.gz', compression='gzip', sep='\t', nrows=1000)
title = pd.read_csv('https://datasets.imdbws.com/title.akas.tsv.gz', compression='gzip', sep='\t', nrows=1000)
basics = pd.read_csv('https://datasets.imdbws.com/title.basics.tsv.gz', compression='gzip', sep='\t', nrows=1000)
crew = pd.read_csv('https://datasets.imdbws.com/title.crew.tsv.gz', compression='gzip', sep='\t', nrows=1000)
episode = pd.read_csv('https://datasets.imdbws.com/title.episode.tsv.gz', compression='gzip', sep='\t', nrows=1000),
principals = pd.read_csv('https://datasets.imdbws.com/title.principals.tsv.gz', compression='gzip', sep='\t', nrows=1000)
ratings = pd.read_csv('https://datasets.imdbws.com/title.ratings.tsv.gz', compression='gzip', sep='\t', nrows=1000)

names.to_sql('test_names', pgSQLengine, if_exists='replace')
title.to_sql('test_names', pgSQLengine, if_exists='replace')
basics.to_sql('test_names', pgSQLengine, if_exists='replace')
crew.to_sql('test_names', pgSQLengine, if_exists='replace')
episode.to_sql('test_names', pgSQLengine, if_exists='replace')
principals.to_sql('test_names', pgSQLengine, if_exists='replace')
ratings.to_sql('test_names', pgSQLengine, if_exists='replace')
                            

