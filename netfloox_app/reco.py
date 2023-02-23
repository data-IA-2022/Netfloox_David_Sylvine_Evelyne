import pandas as pd
from sqlalchemy import create_engine
import yaml # credentials:
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def concat_features(row):
        return(row['genres'].replace(",", " ") + " " + row['nconst'].replace(",", " "))
    
def main(film):
    
    # Récup des info de connection
    with open('../config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    #print(config)

    cfg=config['PG']

    # Connection à BDD
    url = "{driver}://{user}:{password}@{host}/{database}".format(**cfg)
    engine = create_engine(url)

    df = pd.read_sql("""SELECT "primaryTitle", tconst, genres, nconst 
                     FROM title_basics A 
                     LEFT JOIN grouped_name_basics B ON (A.tconst=B."knownForTitles") 
                     WHERE "titleType"='movie';
                     """, engine)

    df.fillna(value='', inplace=True)

    df['movie_features'] = df.apply(concat_features, axis=1)

    # Déclaration de la méthode de vectorisation et application
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df['movie_features'])

    # Input provisoire du film choisi par l'utilisateur

    film_index = df['primaryTitle'].tolist().index(film)

    # Calcul des similarités
    cosine_sim = cosine_similarity(X=count_matrix, Y=count_matrix[film_index])

    # Transformation en un dataframe avec les titres des films
    similarities = pd.DataFrame(cosine_sim)
    similarities = pd.concat([df.iloc[:,0], similarities], axis=1)

    # Sélection des 5 films les plus similaires
    similarities = similarities.sort_values(by=[0], ascending=False)
    film_list = similarities['primaryTitle'].tolist()[1:6]

    return film_list

if __name__ == '__main__':
    main()