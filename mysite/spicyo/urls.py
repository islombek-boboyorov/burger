from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard/', include('dashboard.urls')),
    path('register/', views.register, name="register"),
    path('login/', views.login_pas, name="login_pas"),
    path('about/', views.about, name="about_list"),
    path('index/', views.index, name="index_list"),
    path('blog/', views.blog, name="blog_list"),
    path('contact/', views.contact, name="contact_list"),
    path('recipe/', views.recipe, name="recipe_list"),
]

