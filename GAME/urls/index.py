from django.urls import path, include
from GAME.views.index import index

urlpatterns = [
        path("", index, name="index"),
        path("menu/", include("GAME.urls.menu.index")),
        path("playground/",include("GAME.urls.playground.index")),
        path("settings/",include("GAME.urls.settings.index")),
<<<<<<< HEAD
        ]
=======
]
>>>>>>> 30b51107dc5a042037bc39adc01ab5721e24d030
