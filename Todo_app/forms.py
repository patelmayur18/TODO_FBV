from django import forms
from . models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name','due_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control','placeholder':'mm/dd/yyyy'}),
        }