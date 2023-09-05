

from info.models import *
from rest_framework import serializers
from info.models import Batch, Dept

        

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
    department_id = serializers.IntegerField(source='id')
    department_name = serializers.CharField(source='name')
    class Meta:
        model = Dept
        fields = ["department_id","department_name"]