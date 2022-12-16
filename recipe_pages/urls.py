from django.urls import path
from .views import searchPage, viewRecipePage, indexPage, uploadPage, edit, editPage, delete

urlpatterns = [
    path("", indexPage, name="index"),
    path("upload/", uploadPage, name="uploadPage"),
    path("search/", searchPage, name="searchPage"),
    path("viewrecipe/<str:recipe_name>", viewRecipePage, name="viewrecipePage"),
    path("edit/<str:recipe_name>", edit, name="edit"),
    path("editpage/<str:recipe_name>", editPage, name="editPage"),
    path('delete/<str:recipe_name>', delete, name='delete')
]