from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm

def home(request):
    return render(request, 'core/home.html') 

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save() 
            login(request, user) # log the user in
            return redirect('home') # send the user back home
    else:
        form = SignUpForm() # otherwise create an empty instance of the signup form
    
    return render(request, 'core/register.html', {'form': form})

