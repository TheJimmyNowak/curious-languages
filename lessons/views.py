from django.shortcuts import render
from .models import Courses, Lessons
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    args = {'Courses': Courses.objects.all()[:3]}
    return render(request, 'courses.html', args)


def course(request, course_id):
    try:
        args = {
            'course': Courses.objects.get(courseId=course_id),
            'lessons': Lessons.objects.all().filter(language_id=course_id)
        }
    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    return render(request, 'course.html', args)

