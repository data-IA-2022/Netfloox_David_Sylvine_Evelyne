from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import yaml
import os, glob

# main function
def main():
    # open config.yaml
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
        
    cfg=config['PG']
    print(cfg)

    url = "{driver}://{user}:{password}@{host}/{database}".format(**cfg)
    print('URL', url)
    
    engine = create_engine(url)
    # load with pandas 
    conv1 = lambda x: np.nan if x == '\\N' else x # put NaN
    os.chdir("datasets")
    fns = glob.glob("*.gz")
    
    for fn in fns :
        name = '_'.join(fn.split('.')[:2])
        print(name)
        if name != 'title_crew':
            continue
        df = pd.read_csv(fn, 
                         index_col=0,
                         sep='\t',
                         compression='gzip', 
                         encoding='utf-8', 
                         low_memory=False, 
                         chunksize=100000, 
                         quoting=3, 
                         quotechar='')
        i = 0
        for chunk in df:
            chunk = chunk.applymap(conv1)
            if i == 0:
                chunk.to_sql(name, engine, if_exists='replace')
            else:
                chunk.to_sql(name, engine, if_exists='append')
            i += 1
            print(f"{name}----{i}")
    print("data sent to database")
if __name__ == '__main__':
    main()