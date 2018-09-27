from django import forms
from accounts.models import UsersLevels


class UserLevelForm(forms.ModelForm):
    class Meta:
        model = UsersLevels
        fields = ['userLevel']


class DictionarySearcher(forms.Form):
    word = forms.CharField(required=True, max_length=50)
