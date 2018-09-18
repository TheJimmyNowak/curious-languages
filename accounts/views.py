from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import SignUpForm


def index(request):
    return HttpResponse("DUPA")


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/lessons')
    else:
        form = SignUpForm()
    return render(request, 'accounts/register_form.html', {'form': form})


def profile(request):
    return render(request, 'accounts/profile.html')