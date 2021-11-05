from django.urls import path, include
from GAME.views.index import index

urlpatterns = [
        path("", index, name="index"),
        path("menu/", include("GAME.urls.menu.index")),
        path("playground/",include("GAME.urls.playground.index)),
        path("settings/",include("GAME.urls.settings.index)),
        ]
