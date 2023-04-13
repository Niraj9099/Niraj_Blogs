from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import blog_model, ContactForm
from tinymce.widgets import TinyMCE

class UserCreateForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Conform Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
                   'first_name':forms.TextInput(attrs={'class':'form-control'}),
                   'last_name':forms.TextInput(attrs={'class':'form-control'}),
                   'email':forms.EmailInput(attrs={'class':'form-control'})
                   }

class Addpost(forms.ModelForm):
    class Meta:
        model = blog_model
        fields = ['title', 'disc', 'img']
        widgets = {'title':forms.Textarea(attrs={'class':'title_fild form-control'}),
                   'disc':forms.Textarea(attrs={'class':'img-fluid form-control'}),
                   }

class Contact_Form(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = '__all__'
        widgets = {'full_name':forms.TextInput(attrs={'class':'name form-control'}),
                   'email':forms.EmailInput(attrs={'class':'email form-control'}),
                   'message':forms.Textarea(attrs={'class':'message form-control'}),
                   }
