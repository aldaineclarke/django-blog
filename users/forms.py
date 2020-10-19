from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
# We are creating a form for the register page to create a user account
# In order to do that we need to create a model-like form  which will inherit from the UserCreationForm
class UserRegisterForm(UserCreationForm):
    # This is a customized form, simply because we want only certain field, or even more fields than what was given with the UserCreationForm class/form. By design the UserCreationForms give us the email password and confirmation, so all we need to do first is to create an instance of the form field that we need.
    email = forms.EmailField()

    # This class meta is a bit quirky, but based on my understanding, it just provides the class with more information about the class
    class Meta:
        # This tells the model/table that will be affected by the form when its used
        model = User
        # This tells the form, that it will have a list of these fields. pasword1 and password2 refers to verifying the password
        fields = ['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    
    email = forms.EmailField()

    class Meta:
        
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    
    image = forms.ImageField()

    class Meta:
        
        model = Profile
        fields = ['image']