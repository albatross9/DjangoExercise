from django import forms
from .models import Amsuser
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    username = forms.CharField(max_length=64, label="사용자 이름")
    password = forms.CharField(widget=forms.PasswordInput, label="비밀번호")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            amsuser = Amsuser.objects.get(username=username)

            if not check_password(password, amsuser.password):
                self.add_error('password', '비번틀렷다')
