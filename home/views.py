from django.shortcuts import render
from .models import Movie
def index(request):
    listMovies =  Movie.objects.all()
    data = {'listMovies': listMovies}
    return render(request, 'pages/home.html', data)
