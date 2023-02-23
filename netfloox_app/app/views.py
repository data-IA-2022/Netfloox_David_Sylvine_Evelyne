from django.shortcuts import render
from reco import main
import pandas as pd
import numpy as np
import os 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
# Create your views here.

def home(request):
    return render(request, 'index.html')

def reco(request):
    if request.method == 'POST':
        title = request.POST['recommandation']
        list_film = main(title)
        return render(request, 'recommandation.html', context={
            "reco": '\n'.join(list_film),
            "len" : len(list_film),
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
        print(request.POST)
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
        
        print(nconst_actor["nconst"].iat[0])
        print(nconst_actres)
        print(nconst_dir)
        print(nconst_producer)
        
        list_nconst = [nconst_actor['nconst'].iat[0],
                       nconst_actres['nconst'].iat[0],
                       nconst_producer['nconst'].iat[0],
                       nconst_dir['nconst'].iat[0],]
        list_nconst = ' '.join(list_nconst)
        print(list_nconst)
        pickle_file = open("model_reg.pkl", "rb")
        model = pickle.load(pickle_file)
        
        df_submit = pd.DataFrame(data=[[list_nconst, genre, decade, time, vote]], 
                                 columns=['nconst', 'genres', 'decade', 'runtimeMinutes', 'numVotes'])
        print(df_submit)
        prediction = model.predict(df_submit)
        print(prediction)
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