from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from .forms import PersonalForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('personal')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def personal(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('home')  # Redirect to a success page
    else:
        form = PersonalForm()

    return render(request, 'users/personal.html', {'form': form})