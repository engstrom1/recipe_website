# Create your views here.

from django.shortcuts import HttpResponse

    
def uploadPage(request) :
    # will include upload image/type in recipe functionality 
    return HttpResponse('This page will include the ability to type in a recipe or (hopefully) upload an image')

def searchPage(request):
    # will allow users to search recipe database 
    return HttpResponse("This will be the search page, where you can search the recipe database")

def indexPage(request) :
    # will include about the website  
    return HttpResponse('Welcome to the Index Page. It will include information about the website')