from django import forms
from .models import job

class JobForm(forms.ModelForm):
    job_title = forms.CharField(label='Job Title', 
    widget=forms.TextInput(attrs={'placeholder': 'Enter Job Title'}),)
    company_name = forms.CharField(label='Company Name', 
    widget=forms.TextInput(attrs={'placeholder': 'Enter Company Name'}),)
    salary = forms.DecimalField(label='Salary', required=True, 
    widget=forms.NumberInput(attrs={'class': 'form-salary'}),)
    job_description = forms.CharField(label='Job Description', 
    widget=forms.TextInput(attrs={'placeholder': 'Enter Job Description'}),)
    
    class  Meta:
        model = job
        fields = ['job_title', 'company_name', 'salary', 'job_description']
