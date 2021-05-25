from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from spicyo.models import *
from spicyo.forms import *


def login_required_decorator(f):
    return login_required(f, login_url='login')


@login_required_decorator
def dashboard_page(request):
    return render(request, 'dashboard/index.html')


def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/login.html')


def dashboard_logout(request):
    logout(request)
    return redirect('login')


def recipe_list(request):
    recipes = Recipes.objects.all()
    ctx = {
        "recipes": recipes
    }
    return render(request, 'dashboard/recipe/list.html', ctx)


def recipe_create(request):
    model = Recipes()
    form = RecipesForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('recipe_lists')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/recipe/form.html', ctx)


def recipe_edit(request, pk):
    model = Recipes.objects.get(id=pk)
    form = RecipesForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('recipe_lists')
        else:
            print(form.errors)
    ctx = {
        'form': form
    }
    return render(request, 'dashboard/recipe/form.html', ctx)


def recipe_delete(request, pk):
    model = Recipes.objects.get(id=pk)
    model.delete()
    return redirect('recipe_lists')


def about_list(request):
    abouts = About.objects.all()
    ctx = {
        "abouts": abouts
    }
    return render(request, 'dashboard/about/list.html', ctx)


def about_create(request):
    model = About()
    form = AboutForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('about_lists')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/about/form.html', ctx)


def about_edit(request, pk):
    model = About.objects.get(id=pk)
    form = AboutForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('about_lists')
        else:
            print(form.errors)
    ctx = {
        'form': form
    }
    return render(request, 'dashboard/about/form.html', ctx)


def about_delete(request, pk):
    model = About.objects.get(id=pk)
    model.delete()
    return redirect('about_lists')


def blog_list(request):
    blogs = Blog.objects.all()
    ctx = {
        "blogs": blogs
    }
    return render(request, 'dashboard/blog/list.html', ctx)


def blog_create(request):
    model = Blog()
    form = BlogForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('blog_lists')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/blog/form.list', ctx)


def blog_edit(request, pk):
    model = Blog.objects.get(id=pk)
    form = BlogForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('blog_lists')
        else:
            print(form.errors)
    ctx = {
        'form': form
    }
    return render(request, 'dashboard/blog/form.html', ctx)


def blog_delete(request, pk):
    model = Blog.objects.get(id=pk)
    model.delete()
    return redirect('about_lists')


def client_list(request):
    clients = Client.objects.all()
    ctx = {
        "clients": clients
    }
    return render(request, 'dashboard/client/list.html', ctx)


def client_create(request):
    model = Client()
    form = ClientForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client_lists')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/client/form.list', ctx)


def client_edit(request, pk):
    model = Client.objects.get(id=pk)
    form = ClientForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client_lists')
        else:
            print(form.errors)
    ctx = {
        'form': form
    }
    return render(request, 'dashboard/client/form.html', ctx)


def client_delete(request, pk):
    model = Client.objects.get(id=pk)
    model.delete()
    return redirect('client_lists')
