import pandas as pd
from sqlalchemy import create_engine
import yaml # credentials:
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def concat_features(row):
        return(row['genres'].replace(",", " ") + " " + row['nconst'].replace(",", " "))
    
def main(film):
    
    df = pd.read_csv('../datasets/basics_knownForTitles_ratings.csv', index_col=0)

    df.drop(columns='tconst', inplace=True)

    df.fillna(value='', inplace=True)

    df.isAdult.replace([0, 1], ['Rated_G_PG_PG-13_R', 'Rated_NC-17'], inplace=True)
    df.decade.replace([202, 201, 200, 199, 198, 197, 196, 195, 194, 193, 192, 191, 190, 189], 
                      ['2020s', '2010s', '2000s', '1990s', '1980s', '1970s', '1960s', '1950s', '1940s', '1930s', '1920s', 
                       'silent-era', 'silent-era', 'silent-era'], inplace=True)


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