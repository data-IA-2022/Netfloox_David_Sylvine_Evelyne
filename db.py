from sqlalchemy import create_engine
import pandas as pd
host="greta-p2-g2.westeurope.cloudapp.azure.com"

pgSQLengine = create_engine(
"postgresql+psycopg2://%s:%s@%s/%s" %
("postgres", "greta2023", host, 'test'))

df = pd.read_csv('https://datasets.imdbws.com/name.basics.tsv.gz', compression='gzip', sep='\t', nrows=10)
df.to_sql('test_names', pgSQLengine)
