from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile  # Make sure this matches your model name

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-black focus:border-transparent',
            'placeholder': 'Enter your password'
        }),
        help_text=''
    )
    
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-black focus:border-transparent',
            'placeholder': 'Confirm password'
        }),
        help_text=''
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['username'].widget.attrs.update({
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-black focus:border-transparent',
            'placeholder': 'Enter your username'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-black focus:border-transparent',
            'placeholder': 'Enter your email'
        })

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile  # Make sure this matches your model name
        fields = ['fullname', 'country']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        placeholders = {
            'fullname': 'Enter your full name',
            'country': 'Which country are you from?',
        }
        
        for field in self.fields:
            if not isinstance(self.fields[field].widget, forms.FileInput):
                self.fields[field].widget.attrs.update({
                    'class': 'w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-black focus:border-transparent',
                    'placeholder': placeholders.get(field, f'Enter your {field}')
                })

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        placeholders = {
            'username': 'Enter your username',
            'password': 'Enter your password'
        }
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-black focus:border-transparent',
                'placeholder': placeholders.get(field, f'Enter your {field}')
            })