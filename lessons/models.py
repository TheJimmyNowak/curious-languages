from django.db import models


class courses (models.Model):
    courseId = models.IntegerField(primary_key=True)
    languageName = models.CharField(max_length=100, default="SOME STRING")
    welcomeString = models.TextField(max_length=150)

    class Meta:
        verbose_name = "Dodaj kurs"
        verbose_name_plural = "Dodaj kurs"

class lessons (models.Model):
    lessonId = models.IntegerField(primary_key=True, default=1)
    language = models.ForeignKey(to=courses, on_delete=models.CASCADE)
    topic = models.TextField(default="a")

    class Meta:
        verbose_name_plural= "Dodaj lekcje"

class wordsDirectory (models.Model):
    languageId = models.ForeignKey(to=lessons, on_delete=models.CASCADE)
    word = models.TextField(max_length=50)
    websiteUsersMeaning = models.TextField(max_length=50)

    class Meta:
        verbose_name_plural= "Dodaj słówka"