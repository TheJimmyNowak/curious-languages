from django.contrib import admin
from lessons.models import Courses
from lessons.models import Lessons
from lessons.models import WordsDictionary

admin.site.register(Courses)
admin.site.register(Lessons)
admin.site.register(WordsDictionary)
