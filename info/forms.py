from django import forms
from .models import ClassDetails, BusSchedule, BusDay

class ClassDetailsForm(forms.ModelForm):
    class Meta:
        model = ClassDetails
        fields = ['department', 'batch', 'section', 'day', 'classCode', 'classStart', 'classEnd', 'classSubject', 'classRoom', 'teacherInit' ]

class BusScheduleForm(forms.ModelForm):
    class Meta:
        model = BusSchedule
        fields = ['day', 'time_of_day', 'bus_number', 'route_name']
    day_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)