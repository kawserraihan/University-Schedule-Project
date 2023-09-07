

from info.models import *
from rest_framework import serializers
from info.models import Batch, Dept
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

        

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

    
    class Meta:
        model = ClassDetails
    #    fields = ['class_id', 'classcode', 'day', 'classsubject', 'classroom', 'classstart', 'classend', 'teacherinit' ]
        fields = ['classCode', 'day', 'classSubject', 'classRoom', 'classStart', 'classEnd', 'teacherInit' ]



class DeptSerializer(serializers.ModelSerializer):
    department_id = serializers.IntegerField(source='id')
    department_name = serializers.CharField(source='name')
    
    
    
    class Meta:
        model = Dept
        fields = ["department_id","department_name"]