from django.shortcuts import render
from reco import main
import pandas as pd
import numpy as np
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
    df = pd.read_csv('/home/dakoro/Data_IA/TP/Netfloox_David_Sylvine_Evelyne/datasets/data_regression.csv')
    list_dir = [name for name in df['directors_name'].unique()]
    list_actor = [name for name in df['actors'].unique()]
    list_actress = [name for name in df['actress'].unique()]
    vec = CountVectorizer()
    genres = vec.fit_transform(df['genres'].dropna()).toarray()
    genres = pd.DataFrame(data = genres , columns = vec.get_feature_names_out())
    genres = [item for item in genres.columns]
    
    # request 
    if request.method == 'POST':
        print(request.POST)
        director = request.POST['dir']
        actor = request.POST['actor']
        actress = request.POST['actress']
        time = request.POST['time']
        decade = request.POST['decade']
        genre = request.POST['genre']
        
        pickle_file = open("model_reg.pkl", "rb")
        
        model = pickle.load(pickle_file)
        
        submit = pd.DataFrame(data=[[director, actor, actress, time, decade, genre]], 
                              columns=['directors_name', 'actors', 'actress', 'runtimeMinutes', 'decade', 'genres'])
        result = model.predict(submit)
        return render(request, 'popularity.html', context={'prediction': np.round(result[0], 2)})
    else: 
        return render(request, 'popularity.html', context={
            "directors": list_dir,
            "actors": list_actor,
            "actress": list_actress,
            "genres": genres,
            })