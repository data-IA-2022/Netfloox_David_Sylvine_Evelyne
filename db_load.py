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
    tab_list = []
    os.chdir("datasets")
    for fn in glob.glob("*.gz"):
        tab_list.append('_'.join(fn.split('.')[:2]))
    print(tab_list)
    index = 0
    fns = glob.glob("*.gz")
    for fn in fns :
        i = 0
        print(fn)
        condition = (fn == fns[2]) # fichier 3 génère un erreur, il sera ajouter séparement
        if condition:
            i += 1
            index += 1
            continue
        df = pd.read_csv(fn, sep='\t', compression='gzip', encoding='utf-8', low_memory=False, chunksize=100000)
        
        for chunk in df:
            chunk.applymap(conv1)
            if i == 0:
                chunk.to_sql(tab_list[index], engine, if_exists='replace')
            else:
                chunk.to_sql(tab_list[index], engine, if_exists='append')
            i += 1
            print(f"{tab_list[index]}----{i}")
        index += 1

if __name__ == '__main__':
    main()