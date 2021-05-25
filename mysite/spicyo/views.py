from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


def login_required_decorator(f):
    return login_required(f, login_url="login")


# @login_required_decorator
def home(request):
    return render(request, 'fronted/spicyo/index.html')


def login_pas(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            print(555555)
            login(request, user)
            return redirect('home')
    return render(request, 'fronted/login.html')


def about(request):
    abouts = About.objects.all()
    ctx = {
        "abouts": abouts
    }
    return render(request, 'fronted/spicyo/about.html', ctx)


def index(request):
    return render(request, 'fronted/spicyo/index.html')


def blog(request):
    blogs = Blog.objects.all()
    ctx = {
        "blogs": blogs
    }
    return render(request, 'fronted/spicyo/blog.html', ctx)


def recipe(request):
    recipes = Recipes.objects.all()
    ctx = {
        "recipes": recipes
    }
    return render(request, 'fronted/spicyo/recipe.html', ctx)


def register(request):
    model = User()
    form = UserForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            model = form.save()
            print(model)
            return redirect('home')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'fronted/register.html', ctx)


def contact(request):
    reference = Reference()
    if request.POST:
        reference.name = request.POST.get("Name")
        reference.email = request.POST.get("Email")
        reference.phone = request.POST.get("Phone")
        reference.message = request.POST.get("Message")
        reference.save()
    return render(request, "fronted/spicyo/contact.html")

