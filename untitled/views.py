from django.shortcuts import render

def home(request):

    args = {'userIsLogged': False}

    if request.user.is_authenticated:
        args['userIsLogged'] = True

    return render(request, '../templates/home/index.html', args)
