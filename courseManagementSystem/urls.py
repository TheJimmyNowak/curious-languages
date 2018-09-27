from django.urls import path
from . import views


urlpatterns = [
    path('lesson', views.add_lesson, name="addLesson")
]