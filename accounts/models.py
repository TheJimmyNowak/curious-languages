from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import names as Names


class UserProfiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40)
    password = models.CharField(max_length=100)

    PREMIUM_USER = 'Pr'
    STANDARD_USER = 'Std'

    userTypes={
        (PREMIUM_USER, Names.Accounts.PREMIUM_USER),
        (STANDARD_USER, Names.Accounts.STANDARD_USER)
    }
    userType = models.CharField(choices=userTypes, max_length=2)

    userLevelChoices = {
        (Names.Lessons.BEGINNER, Names.Lessons.Beginner),
        (Names.Lessons.INTERMEDIATE, Names.Lessons.Intermediate),
        (Names.Lessons.ADVANCED, Names.Lessons.Advanced)
    }
    userLevel = models.CharField(choices=userLevelChoices, max_length=2)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        userProfile = UserProfiles.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)

