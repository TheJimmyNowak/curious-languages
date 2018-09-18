from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from lessons.models import Courses
import names as Names


class UserProfiles(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=40)

    PREMIUM_USER = 'Pr'
    STANDARD_USER = 'Std'

    userTypes= {
        (PREMIUM_USER, Names.Accounts.PREMIUM_USER),
        (STANDARD_USER, Names.Accounts.STANDARD_USER)
    }
    userType = models.CharField(choices=userTypes, max_length=2)


class UsersLevels(models.Model):
    userId = models.ForeignKey(to=UserProfiles, on_delete=models.CASCADE)
    courseId = models.ForeignKey(to=Courses, on_delete= models.CASCADE)

    userLevelChoices = {
        (Names.Lessons.BEGINNER, Names.Lessons.Beginner),
        (Names.Lessons.INTERMEDIATE, Names.Lessons.Intermediate),
        (Names.Lessons.ADVANCED, Names.Lessons.Advanced)
    }
    userLevel = models.CharField(choices=userLevelChoices, max_length=2)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        creating_model = UserProfiles.objects.create(user=kwargs['instance'])
        a = User.objects.get(id=kwargs['instance'].id)
        creating_model.username = a.username
        creating_model.save()


post_save.connect(create_profile, sender=User)

