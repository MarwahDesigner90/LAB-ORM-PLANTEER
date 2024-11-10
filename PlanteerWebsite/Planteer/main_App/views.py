from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Contact 
from Plants_App.models import Plants
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

def home_view(request: HttpRequest) -> HttpResponse:
    plants = Plants.objects.all().order_by('-created_at') 
    return render(request, 'main/home.html', {'plants': plants})

def contact_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        name = request.POST.get('first_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:  
            Contact.objects.create(name=name, email=email, message=message)
            return redirect('home')  # Use redirect instead of render for redirecting

    return render(request, "main/contact.html") 

def messages_view(request: HttpRequest) -> HttpResponse:
    messages_list = Contact.objects.all().order_by('-created_at')  
    paginator = Paginator(messages_list, 10)  
    page_number = request.GET.get('page')

    try:
        messages = paginator.page(page_number)
    except PageNotAnInteger:
        messages = paginator.page(1)  
    except EmptyPage:
        messages = paginator.page(paginator.num_pages)
    return render(request, "main/messages.html", {'messages': messages})

