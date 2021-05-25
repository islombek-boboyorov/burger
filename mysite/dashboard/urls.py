from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_page, name="dashboard"),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),

    path('recipe/list/', views.recipe_list, name="recipe_lists"),
    path('recipe/add/', views.recipe_create, name="recipe_add"),
    path('recipe/<int:pk>/edit/', views.recipe_edit, name="recipe_edit"),
    path('recipe/<int:pk>/delete/', views.recipe_delete, name="recipe_delete"),

    path('about/list/', views.about_list, name="about_lists"),
    path('about/add/', views.about_create, name="about_add"),
    path('about/<int:pk>/edit/', views.about_edit, name="about_edit"),
    path('about/<int:pk>/delete/', views.about_delete, name="about_delete"),


    path('blog/list/', views.blog_list, name="blog_lists"),
    path('blog/add/', views.blog_create, name="blog_add"),
    path('blog/<int:pk>/edit/', views.blog_edit, name="blog_edit"),
    path('blog/<int:pk>/delete/', views.blog_delete, name="blog_delete"),

    path('client/list/', views.client_list, name="client_lists"),
    path('client/add/', views.client_create, name="client_add"),
    path('client/<int:pk>/edit/', views.client_edit, name="client_edit"),
    path('client/<int:pk>/delete/', views.client_delete, name="client_delete"),
]
