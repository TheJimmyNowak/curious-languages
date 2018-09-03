from django.shortcuts import render


# Create your views here.
def index(request):
    print(request.get_full_path()+"templates/kursy/index.html")
    return render(request, 'kursy/index.html')
