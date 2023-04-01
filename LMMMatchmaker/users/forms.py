from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    
    error_css_class = 'errorClass'
    
    email = forms.EmailField(widget= forms.TextInput(attrs={'placeholder':'Enter your Email'}), label='')
    username = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter a new Username'}), label='')
    first_name = forms.CharField(max_length=50,required=True, widget= forms.TextInput(attrs={'placeholder':'Enter your first name'}), label='')
    last_name = forms.CharField(max_length=50,required=True, widget= forms.TextInput(attrs={'placeholder':'Enter your last name'}), label='')
    password1 = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter a new Password', 'type' : 'password'}), label='')
    password2 = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Confirm your password', 'type' : 'password'}), label='')

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
