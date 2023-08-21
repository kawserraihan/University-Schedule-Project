from django import forms
from .models import ClassDetails

class ClassDetailsForm(forms.ModelForm):
    class Meta:
        model = ClassDetails
        fields = ['department', 'batch', 'section', 'day', 'classCode', 'classStart', 'classEnd', 'classSubject', 'classRoom', 'teacherInit' ]