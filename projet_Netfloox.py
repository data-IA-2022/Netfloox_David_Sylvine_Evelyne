#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 15:24:19 2023

@author: sylvine
"""

from sqlalchemy.types import Integer
import pandas as pd
import numpy as np
import utils


# creation de la BDD MySaQL
# # soit à la main en indiquant les infos a la main
# host="p2-g2.westeurope.cloudapp.azure.com"

# # pour MySQL:
# # mySQLengine = create_engine(
# #     "mysql://%s:%s@%s:3306/test" %
# #     ('root', 'greta2023', host))

# # Pour postgres
# pgSQLengine = create_engine(
#     "postgresql+psycopg2://%s:%s@%s/%s" %
#     ("postgres", "greta2023", host, 'test'))

# Soit en utilisant config yaml pour stocker les infos sur un fichier qu'on ne mettra pas sur github
engine=utils.get_engine()

files=['name.basics', 'title.akas', 'title.basics', 'title.crew', 'title.episode', 'title.principals', 'title.ratings']

# for name in files:
#     print(f"Chargement {name}")
#     df = pd.read_csv(f"data/{name}.tsv.gz", sep='\t', compression='gzip', nrows=1000)
#     print(df.shape)
#     df.to_sql(name.replace('.', '_'), engine, if_exists='replace') # , index=False


# for name in files:
#     print(f"Chargement {name}")
#     df = pd.read_csv(f"https://datasets.imdbws.com/{name}.tsv.gz", sep='\t', compression='gzip', nrows=1000)
#     print(df.shape)
#     df.to_sql(name.replace('.', '_'), engine, if_exists='replace') # , index=False

conv = lambda x: np.nan if x == '\\N' else x

for name in files:
    print(f"Chargement {name}")
    reader = pd.read_csv(f"dataset_Netfloox/{name}.tsv.gz", 
                     sep='\t', 
                     compression='gzip', 
                     chunksize = 10000)
    chunk = 1
    for df in reader:
        df = df.applymap(conv)
        if chunk == 1:
            df.to_sql(name.replace('.', '_'), engine, if_exists='replace')
        else:
            df.to_sql(name.replace('.', '_'), engine, if_exists='append') 
        print(f"table {name} chunk {chunk} done")
        chunk += 1






###############################
# # test sur seulement le fichier name_basics
# conv = lambda x: np.nan if x == '\\N' else x

# reader = pd.read_csv("dataset_Netfloox/name.basics.tsv.gz", 
#                  sep='\t', 
#                  compression='gzip', 
#                  nrows = 1000000,
#                  chunksize = 1000)
#                  # converters={'birthYear':Year_conv , 'deathYear':Year_conv})

# chunk = 1
# for df in reader:
#     df = df.applymap(conv)
#     df.to_sql("name_basics", engine, if_exists='append', 
#               dtype = {"birthYear" : Integer, 
#                        "deathYear" : Integer}) # , index=False
#     print(f"chunk {chunk} done")
#     chunk += 1








