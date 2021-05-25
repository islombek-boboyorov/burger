from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User()
        fields = '__all__'


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login()
        fields = "__all__"


class RecipesForm(forms.ModelForm):
    class Meta:
        model = Recipes()
        fields = "__all__"


class AboutForm(forms.ModelForm):
    class Meta:
        model = About()
        fields = "__all__"


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog()
        fields = '__all__'


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client()
        fields = '__all__'


class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference()
        fields = '__all__'
