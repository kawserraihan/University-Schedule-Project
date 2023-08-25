

from info.models import *
from rest_framework import serializers
from info.models import Batch

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
    class Meta:
        model = Batch
        fields = ['id', 'name']
