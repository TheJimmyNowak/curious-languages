from django.shortcuts import render, redirect
from .models import Courses, Lessons
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from accounts.models import UsersLevels, UserProfiles
from .forms import UserLevelForm


def index(request):
    args = {'Courses': Courses.objects.all()[:3]}
    return render(request, 'lessons/courses.html', args)


def course(request, course_id):

    try:
        args = {
            'course': Courses.objects.get(course_id=course_id),
            'lessons': Lessons.objects.all().filter(language_id=course_id)
        }
    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    if not UsersLevels.objects.filter(userId=request.user.id).exists():
        return redirect('/lessons/course-'+str(course_id)+'/set-user-level')

    return render(request, 'lessons/course.html', args)


def lesson(request, course_id, lesson_id):
    try:
        args = {
            'lesson': Lessons.objects.get(language_id=course_id, lesson_id=lesson_id)
        }
    except ObjectDoesNotExist:
        print('aaa')
        return HttpResponse(status=404)

    return render(request, 'lessons/lesson.html', args)


def dictionary(request, course_id):
    return render(request, 'lessons/dictionary.html')


def set_user_level(request, course_id):

    if request.method == "POST":
        form = UserLevelForm(request.POST)

        print(request.user.id)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.userId = UserProfiles.objects.get(id=request.user.id)
            temp.courseId = Courses.objects.get(course_id=course_id)
            temp.save()
            return redirect('/lessons/course-'+str(course_id))
    else:
        form = UserLevelForm()

    args = {
        'form': form,
        'course': Courses.objects.get(course_id=course_id)
    }

    return render(request, 'lessons/setUserLevel.html', args)
