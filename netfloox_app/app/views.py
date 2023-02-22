from django.shortcuts import render
from reco import main
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