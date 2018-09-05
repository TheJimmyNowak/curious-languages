from django.shortcuts import render

#ready player one
# Create your views here.
def home(request):
    return render(request, '../templates/home/home.html',
    {
        'userIsLogged': False
    })