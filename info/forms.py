import re
from django import forms
from .models import ClassDetails, BusSchedule, BusDay





#------------------- Class Details Form Start-------------------




class ClassDetailsForm(forms.ModelForm):
    class Meta:
        model = ClassDetails
        fields = ['department', 'batch', 'section', 'day', 'classCode', 'classStart', 'classEnd', 'classSubject', 'classRoom', 'teacherInit' ]




            #------------------Format Class start time-------------------



    def clean_classStart(self):
        classStart = self.cleaned_data.get('classStart')
        if not re.match(r'^\d{2}:\d{2}$', classStart):
            raise forms.ValidationError("Class start time should be in 'HH:MM' format.")
        
        return classStart
    
    
            #---------------------------End-----------------------------
    



            #------------------Format Class end time---------------------




    def clean_classEnd(self):
        classEnd = self.cleaned_data.get('classEnd')
        if not re.match(r'^\d{2}:\d{2}$', classEnd):
            raise forms.ValidationError("Class end time should be in 'HH:MM' format.")
        return classEnd
    
    


            #---------------------------End-----------------------------
    




#------------------- Class Details Form End-------------------





#------------------- Bus Schedule Form Start-------------------



    
class BusScheduleForm(forms.ModelForm):
    class Meta:
        model = BusSchedule
        fields = ['day', 'time_of_day', 'bus_number', 'route_name', 'route_type']
    day_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)

