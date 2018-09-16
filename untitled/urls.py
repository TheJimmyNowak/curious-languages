from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('lessons/', include('lessons.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls'))
]
