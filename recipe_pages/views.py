# Create your views here.
from django.shortcuts import render
from django.shortcuts import HttpResponse

def uploadPage(request) :
    # will include upload image/type in recipe functionality 
    return render(request, 'recipe_pages/upload.html')
    #return HttpResponse('This page will include the ability to type in a recipe or (hopefully) upload an image')

def searchPage(request):
    # will allow users to search recipe database 
    return render(request, 'recipe_pages/search.html')

def indexPage(request) :
    # will include about the website  
    return render(request, 'recipe_pages/about.html')