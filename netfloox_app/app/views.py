from django.shortcuts import render
from reco import main
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import RobustScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import metrics
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import CountVectorizer
import os
def load_model():
    parameters = {'model__n_estimators': range(140, 150, 10), 'model__max_depth': range(6,7)}
    df = pd.read_csv('data/basics_knownForTitles_ratings.csv', index_col=0)
    (df.tconst.value_counts() == 1).all()
    df = df.query('numVotes >= 375')
    df = df.dropna()
    df = df.query('isAdult == 0')
    df = df.drop(columns=['tconst', 'primaryTitle','isAdult'], axis=1)
    df['nconst'] = df['nconst'].str.replace(',', ' ')
    df['genres'] = df['genres'].str.replace(',', ' ')   
    column_num = ['decade', 'runtimeMinutes', 'numVotes']
    transfo_num = Pipeline(steps=[
        ('scaling', RobustScaler())
    ])
    column_tex1 = 'genres'
    column_tex2 = 'nconst'
    transfo_tex = Pipeline(steps=[
        ('countvec', CountVectorizer()), 
        ('dr', TruncatedSVD())    
        ])
    preparation = ColumnTransformer(
        transformers=[
            ('data_tex1', transfo_tex , column_tex1),
            ('data_tex2', transfo_tex , column_tex2),
            ('data_num', transfo_num , column_num)
        ])
    pipe = Pipeline(steps=[('preparation', preparation),
                            ('model', GradientBoostingRegressor())])
    grid = GridSearchCV(pipe, parameters, scoring='r2', cv = 5, n_jobs =-1, verbose = 1)
    y = df['averageRating']
    X = df.drop(columns='averageRating')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
    model = grid.fit(X_train, y_train)
    return model

def home(request):
    return render(request, 'index.html')

def reco(request):
    if request.method == 'POST':
        title = request.POST['recommandation']
        list_film = main(title)
        phrase = f'Recommandatation pour le film intitulé : "{title}" '
        return render(request, 'recommandation.html', context={
            "reco": '\n'.join(list_film),
            "len" : len(list_film),
            "phrase": phrase,
            })
    else:
        return render(request, 'recommandation.html')

def pop(request):
    df_actor = pd.read_csv('data/actor_names.csv', index_col=0)
    df_dir = pd.read_csv('data/director_names.csv', index_col=0)
    df_producer = pd.read_csv('data/producer_names.csv', index_col=0)
    df_actress = pd.read_csv('data/actress_names.csv',index_col=0)
    genres = ['action', 'adult', 'adventure', 'animation', 'biography', 'comedy',
       'crime', 'documentary', 'drama', 'family', 'fantasy', 'fi', 'film',
       'history', 'horror', 'music', 'musical', 'mystery', 'news', 'noir',
       'reality', 'romance', 'sci', 'sport', 'thriller', 'tv', 'war',
       'western']
    
    actors = [item for item in df_actor['actor'].unique()]
    directors = [item for item in df_dir['director'].unique()]
    producers = [item for item in df_producer['producer'].unique()]
    actress = [item for item in df_actress['actress'].unique()]
    
    
    if request.method == 'POST':
        producer = request.POST['producers']
        director = request.POST['dir']
        actor = request.POST['actor']
        actres = request.POST['actress']
        genre = request.POST['genre']
        decade = request.POST['decade']
        time = request.POST['time']
        vote = request.POST['vote']
        
        nconst_actor = df_actor[df_actor['actor'] == actor]
        nconst_actres = df_actress[df_actress['actress'] == actres]
        nconst_dir = df_dir[df_dir['director'] == director]
        nconst_producer = df_producer[df_producer['producer'] == producer]
        
        
        list_nconst = [nconst_actor['nconst'].iat[0],
                       nconst_actres['nconst'].iat[0],
                       nconst_producer['nconst'].iat[0],
                       nconst_dir['nconst'].iat[0],]
        list_nconst = ' '.join(list_nconst)
        
        model = load_model()
        
        df_submit = pd.DataFrame(data=[[list_nconst, genre, decade, time, vote]], 
                                 columns=['nconst', 'genres', 'decade', 'runtimeMinutes', 'numVotes'])
        prediction = model.predict(df_submit)
        return render(request, 'popularity.html', context={"genres": genres,
                                                        "actors": actors,
                                                        "directors": directors,
                                                        "producers": producers,
                                                        "actress": actress,
                                                        "prediction": np.round(prediction[0], 1),
                                                        })
    else:
        return render(request, 'popularity.html', context={"genres": genres,
                                                        "actors": actors,
                                                        "directors": directors,
                                                        "producers": producers,
                                                        "actress": actress})
    
def graph(request):
    path="/home/dakoro/Data_IA/TP/Netfloox_David_Sylvine_Evelyne/netfloox_app/static/img/graph"  # insert the path to your directory   
    img_list =os.listdir(path)   
    options = ["Ratings' distribution", "Rating per types", "Types' distribution", "Directors", "Actors", "Actress"]
    return render(request, 'graphique.html', {'images': img_list,
                                              'options': options,})