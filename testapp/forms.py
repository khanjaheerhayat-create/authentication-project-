from django import forms
from numpy.f2py.crackfortran import usermodules
from django.contrib.auth.models import User

class signupForm(forms.ModelForm):
    class Meta:
        model= User
        fields=['username','password','email','first_name','last_name']
