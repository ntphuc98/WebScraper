from django.shortcuts import render
from .models import Detail
def index(request, id):
    id = str(id)
    
    movieDetail = Detail.objects.get(stt = id)
    data = {"detail": movieDetail}
    return render(request, 'pages/detail.html', data)
def nothing(request):
    return render(request, 'pages/detail.html')