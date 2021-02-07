from django import forms
from .models import StudentInfo

class CreateStudent(forms.ModelForm):
    class Meta:
        model = StudentInfo
        exclude = ("student_img", "fathers_img", "mothers_img", )

        widgets = {
            'Student Number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2018-2020'}),
            'First Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Boluwatife'}),
            'Last Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Odedeyi'}),
            'Level': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: jss1'}),
            
        }

