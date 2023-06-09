from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PersonalData
from .models import UserProfile

sliderClass = """h-1 my-2 mt-2.5 bg-gray-200 rounded-lg appearance-none cursor-pointer range-sm dark:bg-gray-700"""
selectClass = """block text-xs md:text-sm font-light py-2.5 px-0 w-full bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:border-gray-700 focus:outline-none focus:ring-0"""
radioButtonClass = """w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"""

class UserRegisterForm(UserCreationForm):
    
    error_css_class = 'errorClass'

    tailwind_class = """peer block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600"""

    email = forms.EmailField(widget=forms.TextInput(attrs={'class': tailwind_class, 'type': 'email', 'placeholder': ' ', 'id': 'floating_email', 'required': True}), label='')
    username = forms.CharField(widget=forms.TextInput(attrs={'class': tailwind_class, 'placeholder': ' ', 'id': 'floating_username', 'required': True}), label='')
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': tailwind_class, 'placeholder': ' ', 'id': 'floating_first_name'}), label='')
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': tailwind_class, 'placeholder': ' ', 'id': 'floating_last_name'}), label='')
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': tailwind_class, 'type': 'password', 'placeholder': ' ', 'id': 'floating_password1', 'required': True, 'data-tooltip-target' : 'tooltip', 'data-tooltip-trigger' : 'click'}), label='')
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': tailwind_class, 'type': 'password', 'placeholder': ' ', 'id': 'floating_password2', 'required': True}), label='')
    gender = forms.ChoiceField(
        label='Gender',
        choices=(
            ('male', 'Male'),
            ('female', 'Female'),
        ),
        widget=forms.RadioSelect(attrs={
            'class': radioButtonClass,
        }),
        required=False,
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'gender']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        if commit:
            user.save()
            user_profile = UserProfile.objects.create(user=user, gender=self.cleaned_data['gender'])
        return user


class PersonalForm(forms.ModelForm):

    age = forms.IntegerField(
        label='Your Age',
        widget=forms.NumberInput(attrs={
            'type': 'range',
            'min': 18,
            'max': 60,
            'value': 18,
            'class': sliderClass,
            'id': 'self-age'
        }),
        initial=18,
        min_value=18,
        max_value=60,
    )
    
    body_type = forms.ChoiceField(
        label='Your Body Type',
        choices=(
            ('', 'Your Body Type'),
            ('Thin', 'Thin'),
            ('Average', 'Average'),
            ('Stout', 'Stout'),
            ('Petite', 'Petite'),
            ('Broad/Athletic', 'Broad/Athletic'),
        ),
        widget=forms.Select(attrs={
            'class': selectClass,
        }),
        initial='',
    )
    
    weight = forms.IntegerField(
        label='Your Weight',
        widget=forms.NumberInput(attrs={
            'type': 'range',
            'min': 60,
            'max': 500,
            'value': 60,
            'class': sliderClass,
            'id': 'self-weight'
        }),
        initial=60,
        min_value=60,
        max_value=500,
    )
    
    height = forms.IntegerField(
        label='Your Height',
        widget=forms.NumberInput(attrs={
            'type': 'range',
            'min': 50,
            'max': 90,
            'value': 50,
            'class': sliderClass,
            'id': 'self-height'
        }),
        initial=50,
        min_value=50,
        max_value=90,
    )
    
    is_muslim = forms.ChoiceField(
        label='Are you Muslim?',
        choices=(
            ('yes', 'Yes'),
            ('no', 'No'),
        ),
        widget=forms.RadioSelect(attrs={
            'class': radioButtonClass,
        }),
        required=True,
    )
    
    muslim_type = forms.ChoiceField(
        label='What type of Muslim?',
        choices=(
            ('Sunni', 'Sunni'),
            ('Shia', 'Shia'),
            ('Other', 'Other'),
        ),
        widget=forms.RadioSelect(attrs={
            'class': radioButtonClass,
        }),
        required=False,
    )
    
    is_converted = forms.ChoiceField(
        label='Are you Muslim since birth or converted?',
        choices=(
            ('Birth', 'Since birth'),
            ('Convert', 'Converted'),
        ),
        widget=forms.RadioSelect(attrs={
            'class': radioButtonClass,
        }),
        required=False,
    )

    convert_time = forms.ChoiceField(
        label='How long have you been Muslim?',
        choices=(
            ('', 'How long have you been Muslim?'),
            ('< 1 Year', '< 1 Year'),
            ('< 2 Years', '< 2 Years'),
            ('< 5 Years', '< 5 Years'),
            ('< 10 Years', '< 10 Years'),
            ('> 10 Years', '> 10 Years'),
        ),
        widget=forms.Select(attrs={
            'class': selectClass,
        }),
        initial='',
        required=False,
    )

    prayers = forms.ChoiceField(
        label='How many of the 5 daily prayers do you do regularly on time?',
        choices=(
            ('', 'How many of the 5 daily prayers do you do regularly on time?'),
            ('Commited (5 Times)', 'Commited (5 Times)'),
            ('Not Commited (1-4 Times)', 'Not Commited (1-4 Times)'),
            ('Not Praying', 'Not Praying'),
        ),
        widget=forms.Select(attrs={
            'class': selectClass,
        }),
        initial='',
    )

    masjid = forms.ChoiceField(
        label='How connected are you with the local mosque?',
        choices=(
            ('', 'How connected are you with the local mosque?'),
            ('Regular (Every Day)', 'Regular (Every Day)'),
            ('Weekly', 'Weekly'),
            ('Only Fridays', 'Only Fridays'),
            ('Occasionally (For Events)', 'Occasionally (For Events)'),
            ('Not Connected', 'Not Connected'),
        ),
        widget=forms.Select(attrs={
            'class': selectClass,
        }),
        initial='',
    )
    
    class Meta:
        model = PersonalData
        fields = '__all__'  # Use all fields from the model
        widgets = {
            'is_muslim': forms.RadioSelect(attrs={'class': radioButtonClass}),
            'muslim_type': forms.RadioSelect(attrs={'class': radioButtonClass}),
            'is_converted': forms.RadioSelect(attrs={'class': radioButtonClass}),
        }
        
    