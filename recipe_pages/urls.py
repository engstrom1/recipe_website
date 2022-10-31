from django.urls import path
from .views import indexPage
from .views import uploadPage
from .views import searchPage

urlpatterns = [
    path("", indexPage, name="index"),
    path("upload/", uploadPage, name="uploadPage"),
    path("search/", searchPage, name="searchPage"),
]