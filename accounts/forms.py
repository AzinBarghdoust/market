from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from accounts.models import CustomUser


class UserAdminCreationForm(forms.Form):
    phone = forms.CharField(max_length=11)
    password = forms.CharField(max_length=128)
    password_conf = forms.CharField(max_length=128)

    def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def clean(self):
        cd = super().clean()
        password = cd.get('password')
        password_conf = cd.get('password_conf')
        if password and password_conf and password != password_conf:
            raise ValidationError('پسوردها یکسان نیستند')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        qs = CustomUser.objects.filter(phone=phone)
        if qs.exists():
            raise ValidationError('شما موبایل از قبل وجود دارد')
        return phone


# class CreateProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['first_name', 'last_name', 'gender', 'email', ]


class LogInForm(forms.Form):
    phone = forms.CharField(max_length=11)
    password = forms.CharField(max_length=128)
