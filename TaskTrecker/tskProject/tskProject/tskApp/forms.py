from django import forms
from .models import Task

class TaskForms(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('__all__')
        labels = {
            'id':'Task Id',
            'title': 'Task Title',
            'description': 'Task Description',
            'timer':"Task Time",
            'status': 'Task Status',
        }
        widgets = {
            'id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g 1'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter description'}),
            'timer': forms.TimeInput(attrs={'class': 'form-control', 'placeholder':'Enter time'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }