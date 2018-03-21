from django import forms
from django.contrib.auth import get_user_model




class ProfileForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=32)
    phone = forms.CharField(label='电话', max_length=32)

    MY_CHOICES = (('FEMALE', '女'),
                  ('MALE', '男')
    )
    gender = forms.ChoiceField(label='用户性别', choices=MY_CHOICES)
    age = forms.IntegerField(label='年龄')
