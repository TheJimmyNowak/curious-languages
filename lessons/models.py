from django.db import models
from names import Lessons as Names


class Courses (models.Model):
    courseId = models.AutoField(primary_key=True)
    languageName = models.CharField(max_length=100, default="SOME STRING")
    welcomeString = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = Names.verbose_name_course


class Lessons (models.Model):
    lessonId = models.AutoField(primary_key=True)
    language = models.ForeignKey(to=Courses, on_delete=models.CASCADE)
    topic = models.CharField(max_length=50, default='a')
    content = models.TextField(max_length=1000000, editable=False, default="HI :D")
    section = models.CharField(max_length=50, default='a')

    class Meta:
        verbose_name_plural = Names.verbose_name_lessons


class WordsDirectory (models.Model):
    languageId = models.ForeignKey(to=Lessons, on_delete=models.CASCADE)
    word = models.CharField(max_length=50, default='Error')
    websiteUserMeaning = models.CharField(max_length=50, default='Error')
    partOfSpeech = models.CharField(max_length=20, default='Error')

    LEVEL_OF_EDUCATION_CHOICES = {
        (Names.BEGINNER, Names.Beginner),
        (Names.INTERMEDIATE, Names.Intermediate),
        (Names.ADVANCED, Names.Advanced)
    }
    levelOfEducation = models.CharField(
        max_length=2,
        choices=LEVEL_OF_EDUCATION_CHOICES,
        default=Names.BEGINNER
    )

    class Meta:
        verbose_name_plural = Names.verbose_name_wordDirectory
