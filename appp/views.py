from django.shortcuts import render

from .models import Category, Worker, Menu  # Import your models

def index(request):
    # Query the database for categories, workers, and menu items
    categories = Category.objects.all()  # Get all categories
    workers = Worker.objects.all()        # Get all workers
    menus = Menu.objects.all()            # Get all menu items

    # Prepare the context dictionary
    context = {
        'categories': categories,
        'workers': workers,
        'menus': menus,
    }

    # Render the template with the context
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')

def booking(request):
    return render(request, 'booking.html')

def contact(request):
    return render(request, 'contact.html')

def menu(request):
    return render(request, 'menu.html')

def services(request):
    return render(request, 'service.html')

def team(request):
    return render(request, 'team.html')

def testimonials(request):
    return render(request, 'testimonial.html')
