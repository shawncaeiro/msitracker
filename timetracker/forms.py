from django import forms

class ProjectForm(forms.Form):
    projects = forms.ModelChoiceField(label='Your name', max_length=100)