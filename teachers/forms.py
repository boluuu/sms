from django import forms
from .models import TeacherInfo

class CreateTeacher(forms.ModelForm):
    class Meta:
        model = TeacherInfo
        fields = "__all__"

        widgets = {
            'Student no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: John Doe'}),
            'First Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Boluwatife'}),
            'Last Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 30'}),
            'Level': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 30'}),
            
            
            
        }