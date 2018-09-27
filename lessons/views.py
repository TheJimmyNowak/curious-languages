from django.shortcuts import render, redirect
from .models import Courses, Lessons, WordsDictionary
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from accounts.models import UsersLevels, UserProfiles
from .forms import UserLevelForm, DictionarySearcher


def index(request):
    args = {'Courses': Courses.objects.all()[:3]}
    return render(request, 'lessons/main.html', args)


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
        return HttpResponse(status=404)

    return render(request, 'lessons/lesson.html', args)


def dictionary(request, course_id):
    form = DictionarySearcher()
    searching_word = None
    word_meaning = None

    if request.method == "POST":
        form = DictionarySearcher(request.POST)

    if form.is_valid():
        searching_word = form.cleaned_data['word']

        word_meaning = WordsDictionary.objects.all().filter(websiteUserMeaning=searching_word)
        word_meaning = list(word_meaning.values_list('word', flat=True))

        if len(word_meaning) == 0:
            try:
                word_meaning = WordsDictionary.objects.all().filter(word=searching_word)
                word_meaning = list(word_meaning.values_list('websiteUserMeaning', flat=True))
            except ObjectDoesNotExist:
                pass

    args = {
        'form': form,
        'searching_word': searching_word,
        'word_meaning': word_meaning
    }
    return render(request, 'lessons/dictionary.html', args)


def set_user_level(request, course_id):
    form = UserLevelForm()

    if request.method == "POST":
        form = UserLevelForm(request.POST)

    if form.is_valid():
            temp = form.save(commit=False)
            temp.userId = UserProfiles.objects.get(id=request.user.id)
            temp.courseId = Courses.objects.get(course_id=course_id)
            temp.save()
            return redirect('/lessons/course-'+str(course_id))

    args = {
        'form': form,
        'course': Courses.objects.get(course_id=course_id)
    }

    return render(request, 'lessons/setUserLevel.html', args)
