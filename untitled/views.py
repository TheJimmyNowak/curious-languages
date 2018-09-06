from django.shortcuts import render

#ready player one
# Create your views here.
def home(request):
    args = {'userIsLogged': False}

    if request.user.is_authenticated:
        args['userIsLogged'] = True

    return render(request, '../templates/home/home.html', args)
