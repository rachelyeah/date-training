from django import forms

class ProfileForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=32)
    phone = forms.CharField(label='电话', max_length=32)

    MY_CHOICES = (('FEMALE', 'Female'),
                  ('MALE', 'Male')
    )
    gender = forms.ChoiceField(label='用户性别', choices=MY_CHOICES)
    age = forms.IntegerField(label='年龄')