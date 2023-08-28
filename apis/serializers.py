

from info.models import *
from rest_framework import serializers
from info.models import Batch, Dept

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceTotal
        fields = '__all__'


class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = '__all__'


class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignTime
        fields = '__all__'
        

class BatchSerializer(serializers.ModelSerializer):
    batch_id = serializers.IntegerField(source='id')
    batch_name = serializers.CharField(source='name')
    
    class Meta:
        model = Batch
        fields = ['batch_id', 'batch_name']
        

class SectionSerializer(serializers.ModelSerializer):
    section_id = serializers.IntegerField(source='id')
    section_name = serializers.CharField(source='name')
    
    class Meta:
        model = Section
        fields = ['section_id', 'section_name']
        
class ClassDetailsSerializer(serializers.ModelSerializer):
    #class_id = serializers.IntegerField(source='id')
    classcode = serializers.CharField(source='classCode')
 #   day = serializers.CharField(source='day')
    classsubject = serializers.CharField(source='classSubject')
    classroom = serializers.CharField(source='classRoom')
    classstart = serializers.CharField(source='classStart')
    classend = serializers.CharField(source='classEnd')
    teacherinit = serializers.CharField(source='teacherInit')
    
    
    
    class Meta:
        model = ClassDetails
    #    fields = ['class_id', 'classcode', 'day', 'classsubject', 'classroom', 'classstart', 'classend', 'teacherinit' ]
        fields = ['classcode', 'day', 'classsubject', 'classroom', 'classstart', 'classend', 'teacherinit' ]

class DeptSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Dept
        fields = ["id","name"]