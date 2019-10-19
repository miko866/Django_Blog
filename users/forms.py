from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # nested namespace from config for UserModels i can change that
    # inherits Usercreates froms
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # Added classes for Django forms  without help_text
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    # nested namespace from config for UserModels i can change that
    # inherits Usercreates froms
    class Meta:
        model = User
        fields = ['username', 'email']

    # Added classes for Django forms  without help_text
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
