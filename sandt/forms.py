from django import forms
from .models import Sandt

class CreateSandt(forms.ModelForm):
    class Meta:
        model = Sandt
        exclude = ("student_img", "fathers_img", "mothers_img", )

        widgets = {
            'Student Number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2018-2020'}),
            'First Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Boluwatife'}),
            'Last Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Odedeyi'}),
            'Level': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: jss1'}),
            'Staff Number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Staff00111'}),
            'Teacher full Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Odedeyi Boluwatife'}),
            
        }

