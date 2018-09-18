from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course-<int:course_id>/set-user-level', views.set_user_level, name='set-user-level'),
    path('course-<int:course_id>/', views.course, name='course'),
    path('course-<int:course_id>/lesson-<int:lesson_id>/', views.lesson, name='lesson'),
    path('course-<int:course_id>/dictionary', views.dictionary, name='directory')
]