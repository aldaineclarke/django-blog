# As you may have known these are modules that will be used but are not found in the current script
from django.shortcuts import render, redirect
from django.contrib import messages
# This forms module was self created and inherits the UserCreationForm class from django.contrib.auth.forms 
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.

# This is the logic for the register path when requested

def register(request):
    """Creates a registering form and validates entry"""
    # When on that site, since there is a form present with a method, it checks and performs a conditional to see what action to do.
    # Based on the method of the request if it is POST then the logic will continue to have data posted/saved
    if request.method == 'POST':
        # We then instanciate the UserRegisterForm with the data that is supplied by the form. It accepts information from the POST request or form.
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # checks if the form data entered is valid based on the requirements listed, if its true then we can go ahead and have this saved to the database.
            form.save()
            # So what is happenning here is that the form object will be formatted with the clean_data method{formatted into a dictionary}. 
            # The code below however attempts to retrieve the username for the form data then stores it into the local variable username.
            username = form.cleaned_data.get('username') 
            # Since all this is being done in the back-end we need to educate the user whether or not we have successfully create the account.
            # Done using messages. This message method retrieved from the django.contrib module will provide an error message based on preference of the developer, whether its a warning, error, or success
            # This takes two arguements, the request and the message to be delivered, must be a string
            messages.success(request, f'Account created for {username}!, Please attempt to login')
            # After all this is completed, we need to return a response to the request given at the beginning of this view/function. What we can do, is to redirect the user to the home page using the redirect functions from our django.shortcuts module, this takes in ofcourse the url path for redirect, which we can use the name of the path instead.
            return redirect('login')

    # Else what it will do is to generate a form and after the data is inputed it will just return a response to the samepath, or refresh the pasge as it may appear
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form} )

@login_required()
def profile(request):
    """Holds the profile info for the logged in user"""        
        
    # checks image to see if its the default image, if it is then we wont have it shown to the user
    
    def profile_check():
        if request.user.profile.image == 'default.jpg':
            return None
        else:
            return request.user.profile

    # Saves the updates to the database
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        user_form = UserUpdateForm(request.POST,instance= request.user )
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
        messages.success(request, f'Your profile has been succesfully updated')

        return redirect('profile')

    else:

        user_form = UserUpdateForm( instance = request.user)
        profile_form = ProfileUpdateForm(instance = profile_check())

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'users/profile.html', context)

   