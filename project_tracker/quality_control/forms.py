from django import forms
from django.forms import ModelForm
from .models import BugReport, FeatureRequest

class BugReportForm(ModelForm):
    class Meta:
        model = BugReport
        fields = ['title', 'description', 'status', 'priority', 'project', 'task']
        widgets = {
            'title': forms.TextInput(attrs={'required': True}),
            'description': forms.Textarea(attrs={'required': True}),
            'project': forms.Select(attrs={'required': True}),
        }

class FeatureRequestForm(ModelForm):
    class Meta:
        model = FeatureRequest
        fields = ['title', 'description', 'status', 'priority', 'project', 'task']
        widgets = {
            'title': forms.TextInput(attrs={'required': True}),
            'description': forms.Textarea(attrs={'required': True}),
            'project': forms.Select(attrs={'required': True}),
        }