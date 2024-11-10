from urllib import request
from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from.models import Plant
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def all_plants_view(request:HttpRequest):
    plants = Plant.objects.all()
    return render(request, "plants/All_plants.html" , {'plants': plants})

def plants_detail_view (request:HttpRequest):
    plants = Plant.objects.get(pk=plant_id)
    return render(request, "plants/Plants_detail.html" ,{'plants': plants})

def new_plants_view (request:HttpRequest):
      # Initialize variables
    name = ''
    about = ''
    used_for = ''
    image = None
    category = ''
    is_edible = False

    if request.method == "POST":
        name = request.POST.get('name', '')
        about = request.POST.get('about', '')
        used_for = request.POST.get('used_for', '')
        image = request.FILES.get('image', None)
        category = request.POST.get('category', '')
        is_edible = request.POST.get('is_edible') == 'on'

        # Create the new plant entry
        new_plant = Plant.objects.create(
            name=name,
            about=about,
            used_for=used_for,
            image=image,
            category=category,
            is_edible=is_edible
        )
        return redirect('main_App:home_view')  

    # Render the form for GET request
    return render(request, "plants/New_plants.html", {
        'name': name,
        'about': about,
        'used_for': used_for,
        'image': image,
        'category': category,
        'is_edible': is_edible,
    })

def update_plants_view (request:HttpRequest):
    plant = Plant.objects.get(pk=plant_id)
    return render(request, "plants/Update_plants.html")

def delete_plants_view(request:HttpRequest , plant_id=int):
        plant= Plant.objects.get(pk=plant_id)

        if request.method=="Post":
         plant.name=request.POST["name"]
         plant.used_for=request.POST["used_for"]
         plant.category=request.POST["category"]
         plant.is_edible=request.POST["is_edible"]
        if"image" in request.FILES:plant.image= request.FILES["image"]
        plant.save()

        return redirect("plants_app:plants_detail_view", plant_id=plant.id)
        # return render(request, "plants/Delete_plants.html" ,{'plant': plant})

def search_plants_view (request:HttpRequest):
    search_query = request.GET.get('search_query')
    if search_query:
        plants = Plant.objects.filter(name__contains=search_query)
    else:
        plants = None

    context = {
        'plants': plants,
        'search_query': search_query
    }
  
    return render(request, "plants/Search_plants.html", context)

