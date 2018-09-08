from django.contrib import admin
from lessons.models import courses
from lessons.models import lessons
from lessons.models import wordsDirectory

admin.site.register(courses)
admin.site.register(lessons)
admin.site.register(wordsDirectory)
