# Create your views here.
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Recipe

def uploadPage(request) :
    if request.method =='POST':
        new_recipe = Recipe()
        new_recipe.recipe_title = request.POST.get('recipe_title').lower()
        new_recipe.ingredients = request.POST.get('ingredient_name')
        new_recipe.preparation = request.POST.get('preparation')
        new_recipe.link = request.POST.get('recipe_link')
        # new_recipe.image = request.POST.get('recipe_image')
        new_recipe.notes = request.POST.get('notes')
        new_recipe.author = request.POST.get('author')
        new_recipe.save()
    return render(request, 'recipe_pages/upload.html')

# def searchPage(request):
#     # will allow users to search recipe database 
#     if request.method == 'POST' :
#         titleName = request.POST.get("recipe_title")
#         recipe = Recipe.objects.filter(recipe_title__icontains=titleName).all()
#     else: 
#         titleName = "x"
#         recipe = "Not Found"

#     context = {
#         "recipes" : recipe,
#         # "message" : error_message
#                     }
#     return render(request, 'recipe_pages/search.html', context)

def searchPage(request) :
    if request.method == 'POST' :
        title = request.POST.get("recipe_title").lower()
        data = Recipe.objects.filter(recipe_title__contains=title).all()
        if len(data) > 0:
            context = {
                "data" : data
            }
            return render(request, 'recipe_pages/search.html', context)
        else:
            errorMessage = True
            context = {
                "errorMessage" : errorMessage
            }
            return render(request, 'recipe_pages/search.html', context)
    else:
        context = {   
        }
        return render(request, 'recipe_pages/search.html', context)
        
def indexPage(request) :
    # will include about the website  
    return render(request, 'recipe_pages/index.html')

            
def editPage(request, recipe_name):
    recipe_data = Recipe.objects.get(recipe_title=recipe_name)
    recipe_name = recipe_data.recipe_title
    recipe_preparation = recipe_data.preparation #.all()
    recipe_ingredients = recipe_data.ingredients #.all()
    recipe_notes = recipe_data.notes #.all()
    recipe_author = recipe_data.author #.all()
    recipe_image = recipe_data.image #.all()
    recipe_link = recipe_data.link #.all()
    context = {
        "record" : recipe_data,
        "name" : recipe_name,
        "preparation" : recipe_preparation,
        "ingredients" : recipe_ingredients,
        "notes" : recipe_notes,
        "author" : recipe_author,
        "image" : recipe_image,
        "link" : recipe_link
    }
    return render(request, 'recipe_pages/edit.html', context)

def viewRecipePage(request, recipe_name) :
    data = Recipe.objects.filter(recipe_title=recipe_name).all()

    context = {
        'our_recipe' : data
    }
      
    return render(request, 'recipe_pages/viewrecipe.html', context )

def edit(request, recipe_name):
    mylog = Recipe.objects.get(recipe_title=recipe_name)
    if request.method == 'POST':
        new_preparation = request.POST['preparation']
        new_ingredients = request.POST['ingredient_name']
        new_recipe_title = request.POST['recipe_title']
        new_notes = request.POST['notes']
        new_author = request.POST['author']
        # new_image = request.POST['image']
        new_link = request.POST['recipe_link']
        mylog.preparation = new_preparation
        mylog.ingredients = new_ingredients
        mylog.recipe_title = new_recipe_title # Food_Ingredient.objects.get(id = id)
        mylog.notes = new_notes
        mylog.author = new_author
        # mylog.image = new_image
        mylog.link = new_link
        mylog.save()
        # return redirect ('http://127.0.0.1:8000/')
    context={
        'record': mylog
    }
    return render(request, 'recipe_pages/edit.html', context)


def delete(request, recipe_name) :
    log = Recipe.objects.get(recipe_title=recipe_name)
    log.delete()
    return render (request, 'recipe_pages/index.html')