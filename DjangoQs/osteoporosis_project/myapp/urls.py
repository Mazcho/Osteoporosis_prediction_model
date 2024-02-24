from django.urls import path
from myapp import views

urlpatterns = [
    path("",views.home, name="home"),
    path("tipstrick",views.tipstrick, name="tipstrick"),
    path("app",views.app, name="app")
    #path("author",views.author, name="author")
]