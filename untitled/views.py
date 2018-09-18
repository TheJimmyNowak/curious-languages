from django.shortcuts import redirect


def home(request):
    args = {'userIsLogged': False}

    if request.user.is_authenticated:
        args['userIsLogged'] = True

    return redirect('/lessons')
