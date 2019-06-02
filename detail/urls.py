
from django.urls import path, include
from . import views
urlpatterns = [
    # path('', views.index),
    path('<int:id>', views.index),
    path('', views.nothing),
]