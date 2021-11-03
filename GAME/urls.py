from django.urls import path
from GAME.views import index, play


urlpatterns = [
    path("", index,name="index"),
    path("play/", play, name="play")
]
